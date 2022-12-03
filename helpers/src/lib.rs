use std::{
  fs::File,
  io::{BufRead, BufReader},
  path::Path
};

pub fn get_lines(file: impl AsRef<Path>) -> impl Iterator<Item = String> {
  let file = File::open(file).unwrap();
  let reader = BufReader::new(file);
  reader.lines().map(Result::unwrap)
}
