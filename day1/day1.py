'''
# Part 1
currentCal, maxCal= 0, 0,
file = open("day1.txt", 'r')
for line in file:
  if line == '\n':
    if currentCal > maxCal:
      maxCal = currentCal
    currentCal = 0
    continue
  currentCal += int(line.strip())
print(maxCal)
'''

'''
# Part 2
currentCal, cal1, cal2, cal3= 0, 0, 0, 0
file = open("day1.txt", 'r')
for line in file:
  if line == '\n':
    if currentCal > cal1:
      cal1 = currentCal
    elif (currentCal < cal1) & (currentCal > cal2):
      cal2 = currentCal
    elif (currentCal < cal2) & (currentCal > cal3):
      cal3 = currentCal
    currentCal = 0
    continue
  currentCal += int(line.strip())
  
maxCal = cal1+cal2+cal3
print(maxCal)
'''