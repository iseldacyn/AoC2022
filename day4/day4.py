def contains(array1, array2):
  for i in array1:
    if i in array2:
      continue
    else:
      return False
  return True

def hasAnElem(array1, array2):
  for i in array1:
    if i in array2:
      return True
  return False

def arrange(int1, int2):
  array = []
  for i in range(int2):
    if i+1 < int1:
      continue
    else:
      array.append(i+1)
  return array

file = open("day4.txt", 'r')
lines = file.readlines()
numContained = 0
numWithSameElem = 0

for line in lines:
  line.replace('\n','')
  pairs = line.split(',')
  first = pairs[0].split('-')
  second = pairs[1].split('-')
  first = arrange(int(first[0]),int(first[1]))
  second = arrange(int(second[0]),int(second[1]))
  oneIsTwo = contains(first, second)
  twoIsOne = contains(second, first)
  if oneIsTwo | twoIsOne:
    numContained += 1
  hasSameElem = hasAnElem(first, second)
  if hasSameElem:
    numWithSameElem += 1

print(numContained, numWithSameElem)