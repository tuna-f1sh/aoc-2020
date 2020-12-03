use std::collections::HashSet;

#[aoc_generator(day3)]
pub fn input_generator(input: &str) -> HashSet<u64> {
    input
        .lines()
        .map(|l| l.trim())
        .filter(|l| !l.is_empty())
        .map(|l| l.parse().unwrap())
        .collect()
}

#[aoc(day3, part1)]
pub fn part_01(input: &HashSet<u64>) -> Result<u64, &str> {
    unimplemented!();
}

#[aoc(day3, part2)]
pub fn part_02(input: &HashSet<u64>) -> Result<u64, &str> {
    unimplemented!();
}

#[cfg(test)]
mod tests {
    use super::*;

    const EXAMPLE: &str = "1721\n979\n366\n299\n675\n1456";

    #[test]
    fn part1_example() {
        unimplemented!();
    }

    #[test]
    fn part2_example() {
        unimplemented!();
    }
}
