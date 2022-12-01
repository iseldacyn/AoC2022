# Part 1
currentCal, maxCal, cal2, cal3, = 0, 0, 0, 0
file = open("day1.txt", 'r')

for line in file:
  if line == '\n':
    if currentCal > maxCal:
      maxCal = currentCal
    elif (currentCal < maxCal) & (currentCal > cal2):
      cal2 = currentCal
    elif (currentCal < cal2) & (currentCal > cal3):
      cal3 = currentCal
    currentCal = 0
    continue
  currentCal += int(line.strip())

print(maxCal)
maxCal += cal2+cal3
print(maxCal)