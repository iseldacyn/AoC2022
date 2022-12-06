def hasDuplicate(string):
  result = {}
  for char in string:
    if char in result:
      return True
    else:
      result[char] = 1
  print(result)
  return False

def findMarker(string):
  for i in range(len(string)):
    chars = []
    for n in range(14):
      chars.append(string[i+n])
    if not hasDuplicate(chars):
      return i+14

file = open("day6.txt", 'r')
string = file.readlines()[0]

marker = findMarker(string)
print(marker)