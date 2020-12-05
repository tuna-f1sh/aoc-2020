extern crate log;

use std::collections::HashSet;
use std::iter::FromIterator;

#[aoc_generator(day5)]
pub fn input_generator(input: &str) -> Vec<String> {
    input
        .split("\n")
        .filter(|l| !l.is_empty())
        .map(|l| l.to_string())
        .collect()
}

#[aoc(day5, part1)]
pub fn part_01(input: &[String]) -> u64 {
    let mut highest = 0;

    for pass in input {
        let id = get_seat(pass);
        if id > highest {
            highest = id;
        }
    }

    highest
}

pub fn get_seat_pos(pass: &str, bit_char: char) -> u64 {
    pass
        .chars()
        .rev()
        .enumerate()
        .filter(|(_i, c)| *c == bit_char)
        .map(|(i, _c)| 1 << i)
        .sum()
}

pub fn get_seat(pass: &str) -> u64 {
    let (row_str, col_str) = pass.split_at(7);
    let row = get_seat_pos(row_str, 'B');
    let column = get_seat_pos(col_str, 'R');

    row * 8 + column
}

#[aoc(day5, part2)]
pub fn part_02(input: &[String]) -> u64 {
    let ids: Vec<u64> = input.iter().map(|x| get_seat(x)).collect();
    let ids_set: HashSet<u64> = HashSet::from_iter(ids.iter().cloned());
    let min = ids.iter().min().unwrap();
    let max = ids.iter().max().unwrap();
    let all_ids: HashSet<u64> = (*min..*max + 1).collect();

    let missing: HashSet<_> = all_ids.symmetric_difference(&ids_set).collect();
    let value: Vec<&u64> = missing.into_iter().collect();

    *value[0]
}

#[cfg(test)]
mod tests {
    use super::*;

    const EXAMPLE: &str = "FBFBBFFRLR";

    #[test]
    fn part1() {
        let (row_str, col_str) = EXAMPLE.split_at(7);
        assert_eq!(get_seat_pos(row_str, 'B'), 44);
        assert_eq!(get_seat_pos(col_str, 'R'), 5);
        assert_eq!(get_seat(EXAMPLE), 357);
    }
}
