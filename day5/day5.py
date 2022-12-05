def stackInOrder(m, f, stack):
  tempStack = []
  for i in range(int(m)):
    tempStack.append(stacks[int(f)-1].pop())
  tempStack.reverse()
  return tempStack

file = open("day5.txt", "r")
lines = file.readlines()
stacks = [[],[],[],[],[],[],[],[],[]]
box = False

for line in lines:
  if (line[0]==' ' or line[0]=='[') and line[1]!='1':
    temp = 0
    for i in range(len(line)):
      if i%4 == 1:
        if (line[i] != ' '):
          stacks[temp].append(line[i])
        temp += 1
  elif line[0]=='\n':
    for i in stacks:
      i.reverse()
  elif line[1]!='1':
    _, m, _, f, _, t = line.split(' ')
    t.strip('\n')
    #for i in range(int(m)):
      #stacks[int(t)-1].append(stacks[int(f)-1].pop())
    tempStack = stackInOrder(m, f, stacks)
    for i in tempStack:
      stacks[int(t)-1].append(i)

for i in stacks:
  print(i.pop())