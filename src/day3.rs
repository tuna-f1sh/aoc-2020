const TREE: char = '#';

#[aoc_generator(day3)]
pub fn input_generator(input: &str) -> Vec<String> {
    input
        .lines()
        .map(|l| l.trim())
        .filter(|l| !l.is_empty())
        .map(|l| l.to_string())
        .collect()
}

#[aoc(day3, part1)]
pub fn part_01(input: &[String]) -> u64 {
    let slope = vec![3, 1];
    let line_len = input[0].len();
    let mut hit = 0;

    // scan through lines with slope interval
    for y in (0..input.len()).step_by(slope[1]) {
        // scan along that line in x
        if input[y].chars().nth((slope[0] as usize * y) % line_len).unwrap() == TREE { hit += 1; }
    }

    hit
}

#[aoc(day3, part2)]
pub fn part_02(input: &[String]) -> u64 {
    let slopes = vec![vec![1, 1], vec![3, 1], vec![5, 1], vec![7, 1], vec![1, 2]];
    let line_len = input[0].len();
    let mut ret = 1;

    for slope in slopes {
        let mut hit = 0;
        for y in (0..input.len()).step_by(slope[1]) {
            // scan along that line in x
            if input[y].chars().nth((slope[0] as usize * y) % line_len).unwrap() == TREE { hit += 1; }
        }
        ret *= hit;
    }

    ret
}

#[cfg(test)]
mod tests {
    use super::*;

    const EXAMPLE: &str = "..##.......\n#...#...#..\n.#....#..#.\n..#.#...#.#\n.#...##..#.\n..#.##.....\n.#.#.#....#\n.#........#\n#.##...#...\n#...##....#\n.#..#...#.#";

    #[test]
    fn part1_example() {
        assert_eq!(part_01(&input_generator(&EXAMPLE)), 7);
    }

    // #[test]
    // fn part2_example() {
    //     assert_eq!(part_02(&input_generator(&EXAMPLE)), 336);
    // }
}
