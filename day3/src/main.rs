use helpers::get_lines;

fn main() {
  let lines = get_lines("day3.txt");
  let mut ans1: usize = 0;
  let mut ans2: usize = 0;
  let mut n: u32 = 0;
  let mut first_line: String = "".to_string();
  let mut second_line: String = "".to_string();

  for string in lines{
    let split_at: usize = string.len()/2;
    let first: String = string[0..split_at].to_string();
    let second: String = string[split_at..].to_string();

    ans1 += to_priority_num(&second.chars()
      .filter(|c| first.contains(*c))
      .collect::<Vec<char>>());
    
    if n==0{ first_line = string; n+=1; }
    else if n==1{ second_line = string; n+=1; }
    else{
      let third_line: String = string;
      ans2 += to_priority_num(&third_line.chars()
        .filter(|c| second_line.contains(*c))
        .filter(|c| first_line.contains(*c))
        .collect::<Vec<char>>());
        n = 0;
    }
  }
  
  println!("Answer 1: {}", ans1);
  println!("Answer 2: {}", ans2);
}

fn to_priority_num(vec: &Vec<char>) -> usize{
  let alphabet: Vec<char> = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ".to_string()
    .chars()
    .collect();
  alphabet.into_iter().position(|c| c==vec[0]).unwrap() + 1
}