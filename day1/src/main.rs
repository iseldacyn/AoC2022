use helpers::get_lines;

fn main() {
  let lines = get_lines("day1.txt");
  let mut ans: Vec<i32> = vec![];
  let mut temp_int: i32 = 0;

  for int in lines {
    if int == "" {
      ans.push(temp_int);
      temp_int = 0;
      continue;
    }
    temp_int += int.parse::<i32>().unwrap();
  }

  ans.sort();
  ans.reverse();
  println!("Answer 1: {}", ans[0]);
  println!("Answer 2: {}", ans[0]+ans[1]+ans[2]);
  println!("Hello! :3")
}