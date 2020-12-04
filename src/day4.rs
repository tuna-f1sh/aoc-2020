extern crate regex;
extern crate log;

use lazy_static::lazy_static;
use regex::Regex;
use std::collections::HashSet;

#[aoc_generator(day4)]
pub fn input_generator(input: &str) -> Vec<String> {
    input
        .split("\n\n")
        .filter(|l| !l.is_empty())
        .map(|l| l.to_string())
        .collect()
}

#[aoc(day4, part1)]
pub fn part_01(input: &[String]) -> u64 {
    let required_fields: Vec<&'static str> = vec!["byr:", "iyr:", "eyr:", "hgt:", "hcl:", "ecl:", "pid:"];
    let mut ret = 0;

    // I want to get matches from this and check all present from required fields but doesn't seem to return list of matches, just whole string...
    lazy_static! {
        static ref RE: Regex = Regex::new(r"([a-z]{3}:).{7,}").unwrap();
    }

    for i in input {
        if RE.is_match(&i) {
            let mut valid = true;
            for req in &required_fields {
                if i.contains(req) {
                    continue;
                } else {
                    valid = false;
                    break;
                }
            }
            if valid {
                ret += 1;
            }
        }
    }

    ret
}

#[aoc(day4, part2)]
pub fn part_02(input: &[String]) -> usize {
    // this is nicer than part 1
    let required_fields: HashSet<&str> = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"].iter().copied().collect();

    input
        .iter()
        .fold(0, |count, passport| {
            let mut present_fields: HashSet<&str> = HashSet::new();
            if passport
                .split_whitespace()
                .all(|entry| present_fields.insert(entry.split(":").next().unwrap()) && is_valid_entry(entry)) &&
                required_fields.is_subset(&present_fields) {
                count + 1
            } else {
                count
            }
        })
}

// part 2 shamelessly borrowed from https://github.com/ExpoSeed/advent_of_code_2020/blob/main/src/day4.rs to help learn since my solution worked but was getting very messy
fn is_valid_entry(entry: &str) -> bool {
    let mut iter = entry.split(":");
    match iter.next().unwrap() {
        "byr" => match iter.next() {
            Some(value) => match value.parse::<usize>() {
                Ok(number) => number >= 1920 && number <= 2002,
                Err(_) => false,
            }
            None => false
        },
        "iyr" => match iter.next() {
            Some(value) => match value.parse::<usize>() {
                Ok(number) => number >= 2010 && number <= 2020,
                Err(_) => false,
            }
            None => false
        },
        "eyr" => match iter.next() {
            Some(value) => match value.parse::<usize>() {
                Ok(number) => number >= 2020 && number <= 2030,
                Err(_) => false,
            }
            None => false
        },
        "hgt" => match iter.next() {
            Some(value) => match &value[value.len()-2..] {
                "cm" => match (&value[..value.len()-2]).parse::<usize>() {
                    Ok(number) => number >= 150 && number <= 193,
                    Err(_) => false,
                },
                "in" => match (&value[..value.len()-2]).parse::<usize>() {
                    Ok(number) => number >= 59 && number <= 76,
                    Err(_) => false,
                },
                _ => false,
            },
            None => false,

        },
        "hcl" => match iter.next() {
            Some(value) => value.starts_with('#') && value[1..].chars().all(|byte| byte.is_digit(16)),
            None => false,
        },
        "ecl" => match iter.next() {
            Some("amb") | Some("blu") | Some("brn") | Some("gry") | Some("grn") | Some("hzl") | Some("oth") => true,
            _ => false,
        },
        "pid" => match iter.next() {
            Some(value) => value.len() == 9 && value.parse::<usize>().is_ok(),
            None => false,
        },
        "cid" => true,
        _ => panic!("bad field"),
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    const EXAMPLE: &str = "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in";

    const VALID: &str = "pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719";

    const INVALID: &str = "eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007";

    #[test]
    fn part1_example() {
        assert_eq!(part_01(&input_generator(&EXAMPLE)), 2);
    }
    
    #[test]
    fn part2_examples() {
        assert_eq!(part_02(&input_generator(&VALID)), 4);
        assert_eq!(part_02(&input_generator(&INVALID)), 0);
    }

    // #[test]
    // fn part2_example() {
    //     assert_eq!(part_02(&input_generator(&EXAMPLE)).unwrap(), 241861950);
    // }
}
