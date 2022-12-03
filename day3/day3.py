import string

def isIn(first, second):
  for i in first:
    if i in second:
      return alphabet.index(i)+1

def isInThree(first, second, third):
  for i in first:
    if i in second:
      if i in third:
        return alphabet.index(i)+1

file = open("day3.txt", 'r')
lines = file.readlines()
alphabet = list(string.ascii_letters)
ans1, ans2 = 0, 0
n = 0

for line in lines:
  # part 1
  splitat = len(line)//2
  first, second = line[:splitat], line[splitat:-1]
  ans1 += isIn(first, second)
  
  # part 2
  if n==0:
    firstL = line
  if n==1:
    secondL = line
  if n==2:
    thirdL = line
    ans2 += isInThree(firstL, secondL, thirdL)
    n = 0
    continue
  n+=1
  
  



print(f'{ans1}, {ans2}')