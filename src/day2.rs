extern crate regex;
extern crate log;

use std::error::Error;
use regex::Regex;
use log::{debug};

/*
 * Each line gives the password policy and then the password. The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.
 *
 * How many passwords in input are valid?
 */

// parse input as regex, apply to password to check validity

#[derive(Debug, Eq, PartialEq)]
pub struct PassList {
    c: char,
    min: u32,
    max: u32,
    password: String
}

#[aoc_generator(day2)]
pub fn input_generator(input: &str) -> Result<Vec<PassList>, Box<dyn Error>> {
    input
        .lines()
        .map(|l| l.trim())
        .filter(|l| !l.is_empty())
        .map(|l| {
            let (reg, pass) = l.split_at(l.find(':').ok_or(": not found")?);
            let (quantity, c) = reg.split_at(reg.find(' ').unwrap());
            let c = c.trim().chars().nth(0).unwrap();
            let (min, max) = quantity.split_at(quantity.find('-').ok_or("- not found")?);
            let min = min.trim().parse()?;
            let max = max.get(1..).ok_or("max not found")?.trim().parse()?;
            let pass = pass.get(1..).ok_or("password not found")?.trim();
            debug!("day 2 parsed values: {:?} {:?} {:?} {:?}", min, max, c, pass);

            Ok(PassList {
                c,
                min,
                max,
                password: pass.to_string()
            })
        }).collect()
}

#[aoc(day2, part1, regex)]
// this doesn't capture all:
// - looking at capture count doesn't work because might be multiple captures below max
// - need to accumulate len of captures
// - but then same as just matching single char and summing like search
pub fn part_01(input: &[PassList]) -> u64 {
    let mut regex;
    let mut re;
    let mut matches = 0;

    for i in input {
        regex = format!(r"[{}]{{{},{}}}", i.c, i.min, i.max);
        re = Regex::new(&regex).unwrap();
        let mut count = 0;
        debug!("day 2 regex: {:?} for {:?}", re, i);
        // re.captures(&i.password).and_then(|cap| {
        //     count += cap.len();
        //     println!("{:?} {:?}", i.password, count);
        // });
        // if count as u32 <= i.max && count as u32 >= i.min {
        //     matches += 1;
        // }
        // if re.find_iter(&s.password).count() == 1 {
        //     matches += 1;
        //     println!("{:?} is a match", s);
        // }
    }

    matches
}

#[aoc(day2, part1, search)]
pub fn part_01_search(input: &[PassList]) -> u64 {
    let mut matches = 0;

    for i in input {
        let v: Vec<&str> = i.password.as_str().matches(i.c).collect();
        let num = v.len() as u32;
        if num >= i.min && num <= i.max {
            matches += 1;
        }
    }

    matches
}

#[aoc(day2, part2)]
pub fn part_02_search(input: &[PassList]) -> u64 {
    let mut matches = 0;

    for i in input {
        let v: Vec<_> = i.password.as_str().match_indices(i.c).collect();
        let mut found = false;
        for m in v {
            let index = m.0 as u32 + 1; // Be careful; Toboggan Corporate Policies have no concept of "index zero"!
            if index == i.min || index == i.max {
                if found {
                    found = false;
                    break;
                } else {
                    found = true;
                }
            }
        }
        if found { matches += 1; }
    }

    matches
}

#[cfg(test)]
mod tests {
    use super::*;

    const EXAMPLE: &str = "1-3 a: abcde\n1-3 b: cdefg\n2-9 c: ccccccccc";

    #[test]
    fn part1_regex_example() {
        assert_eq!(part_01(&input_generator(EXAMPLE).unwrap()), 2);
    }

    #[test]
    fn part1_search_example() {
        assert_eq!(part_01_search(&input_generator(EXAMPLE).unwrap()), 2);
    }

    #[test]
    fn part2_search_example() {
        assert_eq!(part_02_search(&input_generator(EXAMPLE).unwrap()), 1);
    }
}
