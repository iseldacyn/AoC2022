file = open("day2.txt")
points = 0

for line in file:
  choice = line.split()
  '''
  match choice[1]:
    case 'X':
      points += 1
      if choice[0] == 'A': points += 3
      elif choice[0] == 'C': points += 6
    case 'Y':
      points += 2
      if choice[0] == 'B': points += 3
      elif choice[0] == 'A': points += 6
    case 'Z':
      points += 3
      if choice[0] == 'C': points += 3
      elif choice[0] == 'B': points += 6
  '''
  match choice[0]:
    case 'A':
      match choice[1]:
        case 'X':
          points += 3
        case 'Y':
          points += 4
        case 'Z':
          points += 8
    case 'B':
      match choice[1]:
        case 'X':
          points += 1
        case 'Y':
          points += 5
        case 'Z':
          points += 9
    case 'C':
      match choice[1]:
        case 'X':
          points += 2
        case 'Y':
          points += 6
        case 'Z':
          points += 7

print(points)