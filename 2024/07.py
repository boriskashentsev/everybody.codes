# Part 1

f = open('07.01.input', "r")
input = f.read()
lines = input.split('\n')

contestants = []
numberOfSegmenets = 10
for line in lines:
  energy = 10
  runEnergy = 0
  letter = line.split(':')[0]
  strategy = line.split(':')[1].split(',')
  for i in range(numberOfSegmenets):
    if strategy[i%len(strategy)] == '+':
      energy += 1
    elif strategy[i%len(strategy)] == '-':
      energy -= 1
    runEnergy += energy
  contestants.append([letter, runEnergy])

def sortByEnergyLevel(e):
  return e[1]

contestants.sort(reverse=True, key=sortByEnergyLevel)
print("Part 1: ", ''.join(list(map(lambda x: x[0],contestants))))

# Part 2
test = '.test'
test = ''
f = open ('07.02.loop'+test+'.input', 'r')
input = f.read()
lines = input.split('\n')
loop=''
for i in range(len(lines)):
  if i == 0:
    loop=lines[i]
  else:
    index = round(len(lines[0]) + (len(loop)-len(lines[0]))/2)
    loop=loop[:index]+''.join(list(filter(lambda x: x!= ' ',lines[i][::-1])))+loop[index:]
loop = loop[1:]+loop[0]

f = open('07.02'+test+'.input', "r")
input = f.read()
lines = input.split('\n')

contestants = []
numberOfLoops = 10
for line in lines:
  energy = 10
  runEnergy = 0
  letter = line.split(':')[0]
  strategy = line.split(':')[1].split(',')
  for i in range(numberOfLoops*len(loop)):
    if loop[i%len(loop)] in 'S=':
      if strategy[i%len(strategy)] == '+':
        energy += 1
      elif strategy[i%len(strategy)] == '-':
        energy -= 1
    elif loop[i%len(loop)] == '+':
      energy += 1
    elif loop[i%len(loop)] == '-':
      energy -= 1
    runEnergy += energy
  contestants.append([letter, runEnergy])

contestants.sort(reverse=True, key=sortByEnergyLevel)
print("Part 2: ", ''.join(list(map(lambda x: x[0],contestants))))

# Part 3

f = open ('07.03.loop.input', 'r')
input = f.read()
lines = input.split('\n')
loop=''

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
direction = 0
x = 0
y = 0
isEndOfTheLoop = False

while not isEndOfTheLoop:
  loop += lines[y][x]
  tryNextDirection = False
  if y+dy[direction] in range(len(lines)) and x+dx[direction] in range(len(lines[y+dy[direction]])):
    # Can we go forward
    if lines[y+dy[direction]][x+dx[direction]] == ' ':
      tryNextDirection = True
  else:
    tryNextDirection = True
  # Let's try left direction
  if tryNextDirection:
    tryNextDirection = False
    newDirection = (direction - 1) % len(dx)
    if y+dy[newDirection] in range(len(lines)) and x+dx[newDirection] in range(len(lines[y+dy[newDirection]])):
      if lines[y+dy[newDirection]][x+dx[newDirection]] == ' ':
        tryNextDirection = True
    else:
      tryNextDirection = True
    # Let's try right difrection
    if tryNextDirection:
      newDirection = (direction + 1) % len(dx)
      # Assuming there is always way forward left of right, there is no need to check if there is a way on the left 
      # as it is the last firection we can go
    direction = newDirection
  y = y+dy[direction]
  x = x+dx[direction]
  if lines[y][x] == 'S':
    isEndOfTheLoop = True
loop = loop[1:]+loop[0]

f = open('07.03.input', "r")
input = f.read()
lines = input.split('\n')

def calculateEnergy(loop, strategy):
  numberOfLoops = 2024
  energy = 10
  runEnergy = 0
  for i in range(numberOfLoops*len(loop)):
    if loop[i%len(loop)] in 'S=':
      if strategy[i%len(strategy)] == '+':
        energy += 1
      elif strategy[i%len(strategy)] == '-':
        energy -= 1
    elif loop[i%len(loop)] == '+':
      energy += 1
    elif loop[i%len(loop)] == '-':
      energy -= 1
    runEnergy += energy
  return runEnergy

def strategyReady(choices):
  return len(list(filter(lambda x: choices[x] > 0, choices.keys()))) == 0

def generateStrategy(choices, strategy, loop, energyToBeat, numberOfBetterStrategies):
  if strategyReady(choices):
    if calculateEnergy(loop, strategy) > energyToBeat:
      return numberOfBetterStrategies + 1
    return numberOfBetterStrategies
  else:
    for key in choices.keys():
      if (choices[key] > 0):
        strategy += key
        choices[key] -= 1
        numberOfBetterStrategies = generateStrategy(choices, strategy, loop, energyToBeat, numberOfBetterStrategies)
        strategy=strategy[:len(strategy)-1]
        choices[key] += 1
  return numberOfBetterStrategies


letter = lines[0].split(':')[0]
strategy = lines[0].split(':')[1].split(',')

energyToBeat = calculateEnergy(loop, strategy)

# I couldn't figure out any other solution than Brute Force
numberOfBetterStrategies = generateStrategy({'+':5, '-':3, '=':3}, '', loop, energyToBeat, 0)
print ("Part 3: ", numberOfBetterStrategies)
