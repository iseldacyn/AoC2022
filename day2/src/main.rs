use helpers::get_lines;

fn main() {
  let lines = get_lines("day2.txt");

  let matrix1: Vec<i32> = vec![
    4, 8, 3,
    1, 5, 9,
    7, 2, 6
  ];
  let matrix2: Vec<i32> = vec![
    3, 4, 8,
    1, 5, 9,
    2, 6, 7
  ];

  let mut answer1: i32 = 0;
  let mut answer2: i32 = 0;

  for i in lines{
    let j: Vec<i32> = i.trim()
      .split(' ')
      .map(|s| to_char(s))
      .collect();
    let index: i32 = j[0]*3 + j[1];
    answer1 += matrix1[index as usize];
    answer2 += matrix2[index as usize];
  }

  println!("Answer 1: {}", answer1);
  println!("Answer 2: {}", answer2);

}

fn to_char(string: &str) -> i32 {
  match string{
    "A" | "X" => 0,
    "B" | "Y" => 1,
    "C" | "Z" => 2,
    _ => { eprint!("Error, NaN"); -1 }
  }
}