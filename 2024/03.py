from functools import reduce

# Part 1

f = open('03.01.input', "r")
input = f.read()
lines = input.split('\n')

land = []
for line in lines:
  land += [list(map(lambda x: 0 if x=='.' else 1, line))]

def digging(land, dx, dy):

  isDiggingPossible = True
  level = 0
  while isDiggingPossible:
    level += 1
    isDiggingPossible = False
    for i in range(len(land)):
      for j in range(len(land[i])):
        if land[i][j] == level:
          diggingDeeper = True
          for k in range(len(dx)):
            if i+dy[k] in range(len(land)) and j+dx[k] in range(len(land[i])):
              if land[i+dy[k]][j+dx[k]] < level:
                diggingDeeper = False
            else:
              diggingDeeper = False
          if diggingDeeper:
            land[i][j] = level + 1
            isDiggingPossible = True

  result = 0
  for line in land:
    result += reduce(lambda x,y: x+y, line)
  return result

print('Part 1: ', digging(land,[1, 0, -1, 0],[0, 1, 0, -1]))

# Part 2

f = open('03.02.input', "r")
input = f.read()
lines = input.split('\n')

land = []
for line in lines:
  land += [list(map(lambda x: 0 if x=='.' else 1, line))]

print('Part 2: ', digging(land,[1, 0, -1, 0],[0, 1, 0, -1]))


# Part 3

f = open('03.03.input', "r")
input = f.read()
lines = input.split('\n')

land = []
for line in lines:
  land += [list(map(lambda x: 0 if x=='.' else 1, line))]

print('Part 3: ', digging(land,[1, 1,  0, -1, -1, -1, 0, 1],[0, 1, 1, 1, 0, -1, -1, -1]))