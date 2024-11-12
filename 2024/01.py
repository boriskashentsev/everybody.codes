from functools import reduce

# Part 1

f = open('01.01.input', "r")
input = f.read()

As = len(input.split('A'))-1
Bs = len(input.split('B'))-1
Cs = len(input.split('C'))-1

print('Part 1: ',As*0 + Bs*1 + Cs*3 )

# Part 2

f = open('01.02.input', "r")
input = f.read()

def numberOfPotions(enemy, buddies):
  if (enemy == 'x'):
    return 0
  enemyType = 'ABCD'
  potions = [0,1,3,5]
  index = enemyType.find(enemy)
  return potions[index] + buddies

def lookAtEnemies(enemies):
  if (len(enemies.split('x')) - 1 == len(enemies)):
    return 0
  buddies = len(enemies) - (len(enemies.split('x')) - 1) - 1
  individualPotions = map(lambda enemy: numberOfPotions(enemy, buddies), list(enemies))
  return reduce(lambda x, y: x + y, list(individualPotions))

potions = 0
groups = 2
for i in range(round(len(input)/2)):
  index = i*groups
  enemies= input[index:index+groups]
  potions += lookAtEnemies(enemies)

print("Part 2: ",potions)

# Part 3

f = open('01.03.input', "r")
input = f.read()

potions = 0
groups = 3
for i in range(round(len(input)/groups)):
  index = i*groups
  enemies= input[index:index+groups]
  potions += lookAtEnemies(enemies)

print("Part 3: ", potions)