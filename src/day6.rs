#[aoc_generator(day6)]
pub fn input_generator(input: &str) -> Vec<String> {
    input
        .split("\n\n")
        .filter(|l| !l.is_empty())
        .map(|l| l.to_string())
        .collect()
}

#[aoc(day6, part1)]
pub fn part_01(input: &[String]) -> u32 {
    // we don't need the string represenation so can use char as bit position, store in mask then count the bits in u32 for the number of unique values
    input.iter()
        .map(|g| {
            // first split into group answers but this causes incorrect answer
            // g.lines()
            // .map(|x| {
            //     x.bytes()
            g.bytes()
                    // ensure it's a-z
                    .filter(|char| *char >= b'a' && *char <= b'z')
                    // or with current to only count if unique
                    .fold(0, |num, char| num | 1u32 << (char - b'a'))
                    // count unique
                    .count_ones()
            }).sum::<u32>()
        // }).sum::<u32>()
}

#[aoc(day6, part2)]
pub fn part_02(input: &[String]) -> u32 {
    input.iter()
        .map(|group| {
            group.lines()
                .map(|answer| {
                    answer.bytes()
                        // ensure it's a-z
                        .filter(|char| *char >= b'a' && *char <= b'z')
                        // or with current to only count if unique
                        .fold(0, |num, char| num | 1u32 << (char - b'a'))
                }).fold(!0, |a, b| a & b).count_ones()
        }).sum::<u32>()
}

#[cfg(test)]
mod tests {
    use super::*;

    const EXAMPLE: &str = "abc

a
b
c

ab
ac

a
a
a
a

b";

    #[test]
    fn part1() {
        assert_eq!(part_01(&input_generator(&EXAMPLE)), 11);
    }

    #[test]
    fn part2() {
        assert_eq!(part_02(&input_generator(&EXAMPLE)), 6);
    }
}
