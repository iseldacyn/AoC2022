use std::{
  fs::File,
  io::{BufReader, BufRead},
};

fn main() {
  let file: File = File::open("day1.txt").unwrap();
  let reader: BufReader<File> = BufReader::new(file);
  let lines = reader.lines();
  let mut ans: Vec<i32> = vec![];
  let mut temp_int: i32 = 0;

  for int in lines {
    let temp_string: String = int.unwrap();
    if temp_string == "" {
      ans.push(temp_int);
      temp_int = 0;
      continue;
    }
    temp_int += temp_string.parse::<i32>().unwrap();
  }

  ans.sort();
  ans.reverse();
  println!("Answer 1: {}", ans[0]);
  println!("Answer 2: {}", ans[0]+ans[1]+ans[2]);
  
}