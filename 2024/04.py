# Part 1

def leveling(nails):
  minLength = nails[0]

  result = 0
  for i in range(1,len(nails)):
    if minLength <= nails[i]:
      result += nails[i] - minLength
    else:
      result += (minLength-nails[i])*i
      minLength = nails[i]
  return result

f = open('04.01.input', "r")
input = f.read()
nails = list(map(lambda x: int(x),input.split('\n')))

print('Part 1: ', leveling(nails))

# Part 2

f = open('04.02.input', "r")
input = f.read()
nails = list(map(lambda x: int(x),input.split('\n')))

print('Part 2: ', leveling(nails))

# Part 3

def levelingToSome(nails):
  results = []
  for i in range(len(nails)):
    result = 0
    level = nails[i]
    for nail in nails:
      result += abs(level - nail)
    results += [result]
  return min(results)

f = open('04.03.input', "r")
input = f.read()
nails = list(map(lambda x: int(x),input.split('\n')))

print("Part 3: ", levelingToSome(nails))
