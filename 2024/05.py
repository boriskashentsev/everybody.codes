# Part 1
f = open('05.01.input', "r")
input = f.read()
lines = input.split('\n')

columns = []
for i in range(len(lines[0].split(' '))):
  columns.append([])

for i in range(len(lines)):
  elements = lines[i].split(' ')
  for j in range(len(elements)):
    columns[j].append(int(elements[j]))

for i in range(10):
  index = (i+1) % 4
  element = columns[i%4].pop(0)
  steps = (element - 1) % (len(columns[index])*2)
  if steps > len(columns[index]):
    steps = len(columns[index])*2 - steps
  columns[index] = columns[index][:steps] + [element] + columns[index][steps:]
  
print('Part 1: ', ''.join(list(map(lambda x: str(x[0]),columns))))

# Part 2

f = open('05.02.input', "r")
input = f.read()
lines = input.split('\n')

columns = []
for i in range(len(lines[0].split(' '))):
  columns.append([])

for i in range(len(lines)):
  elements = lines[i].split(' ')
  for j in range(len(elements)):
    columns[j].append(int(elements[j]))

toContinue = True
collection = {}
repetition = 2024
i = 0

while toContinue:
  index = (i+1) % 4
  element = columns[i%4].pop(0)
  steps = (element - 1) % (len(columns[index])*2)
  if steps > len(columns[index]):
    steps = len(columns[index])*2 - steps
  columns[index] = columns[index][:steps] + [element] + columns[index][steps:]
  key = ''.join(list(map(lambda x: str(x[0]),columns)))
  i += 1
  if key in collection.keys():
    collection[key] += 1
  else: 
    collection[key] = 1
  if collection[key] == repetition:  
    toContinue = False
print('Part 2: ', int(key) * i)

# Part 3

f = open('05.03.input', "r")
input = f.read()
lines = input.split('\n')

columns = []
for i in range(len(lines[0].split(' '))):
  columns.append([])

for i in range(len(lines)):
  elements = lines[i].split(' ')
  for j in range(len(elements)):
    columns[j].append(int(elements[j]))

toContinue = True
collection = {}
repetition = 2024
i = 0
maxValue = 0

while toContinue:
  index = (i+1) % 4
  element = columns[i%4].pop(0)
  steps = (element - 1) % (len(columns[index])*2)
  if steps > len(columns[index]):
    steps = len(columns[index])*2 - steps
  columns[index] = columns[index][:steps] + [element] + columns[index][steps:]
  key = ''.join(list(map(lambda x: str(x[0]),columns)))
  i += 1
  
  if key in collection.keys():
    collection[key] += 1
  else: 
    collection[key] = 1
  if maxValue < int(key):
    maxValue = int(key)
  if i == 500000:  
    # This is not the best proof of concept, but solves the task
    toContinue = False

print('Part 3: ', maxValue)