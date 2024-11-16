from functools import reduce

# Part 1

f = open('02.01.input', "r")
input = f.read()
lines = input.split('\n')

runes = lines[0].split(':')[1].split(',')
phrase = lines[2]
result = 0
for rune in runes:
  used = len(phrase.split(rune)) - 1
  result += used

print("Part 1: ", result)

# Part 2

f = open('02.02.input', "r")
input = f.read()
lines = input.split('\n')

words = lines[0].split(':')[1].split(',')
lines = lines[2:]

result = 0
for line in lines:
  color = [0]*len(line)
  for word in words:
    reversedWord = ''.join(reversed(list(word)))
    for i in range(len(line)-len(word)+1):
      part = line[i:i+len(word)]
      if part == word or part == reversedWord:
        for j in range(len(word)):
          color[i+j] = 1
  result += reduce(lambda x,y: x+y, color)

print("Part 2: ", result)

# Part 3

f = open('02.03.input', "r")
input = f.read()
lines = input.split('\n')

words = lines[0].split(':')[1].split(',')
lines = lines[2:]

color = []
for i in range(len(lines)):
  color += [[0]*len(lines[i])]

for word in words:
  reversedWord = ''.join(reversed(list(word)))
  # horizontal search
  for i in range(len(lines)):
    line = lines[i]+lines[i][:len(word)]
    for j in range(len(line)-len(word)+1):
      part = line[j:j+len(word)]
      if part == word or part == reversedWord:
        for k in range(len(word)):
          color[i][(j+k)%len(lines[i])]=1
  # vertical search
  for i in range(len(lines[0])):
    line = ''.join(list(map(lambda x: x[i], lines)))
    for j in range(len(line)-len(word)+1):
      part = line[j:j+len(word)]
      if part == word or part == reversedWord:
        for k in range(len(word)):
          color[j+k][i]=1

result = 0
for line in color:
  result += reduce(lambda x,y: x+y, line)

print("Part 3: ", result)