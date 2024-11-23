def traverseTree(tree, node, path ,paths, separator=''):
  if node in tree.keys():
    for branch in tree[node]:
      if branch=='@':
        paths.append(path+separator+branch)
      elif branch =='ANT' or branch == 'BUG':
        # This feels wrong. As if I was lucky to find the right branch without a tricky edge case.
        paths.append(path+separator+branch)
      else:
        paths = traverseTree(tree, branch, path+separator+branch, paths, separator)
  else:
    paths.append(path)
  return paths

# Part 1

f = open('06.01.input', "r")
input = f.read()
lines = input.split('\n')

tree = {}

for line in lines:
  root = line.split(':')[0]
  branches = line.split(':')[1].split(',')
  tree[root] = branches

paths = traverseTree(tree, 'RR', 'RR', [])

len2paths = {}
for path in paths:
  if len(path) in len2paths.keys():
    len2paths[len(path)].append(path)
  else:
    len2paths[len(path)]=[path]

key = list(filter(lambda x: len(len2paths[x])==1, len2paths.keys()))[0]
print('Part 1: ', len2paths[key][0])

# Part 2

f = open('06.02.input', "r")
input = f.read()
lines = input.split('\n')

tree = {}

for line in lines:
  root = line.split(':')[0]
  branches = line.split(':')[1].split(',')
  tree[root] = branches

paths = traverseTree(tree, 'RR', 'RR', [], ',')

len2paths = {}
for path in paths:
  if len(path) in len2paths.keys():
    len2paths[len(path)].append(path)
  else:
    len2paths[len(path)]=[path]

key = list(filter(lambda x: len(len2paths[x])==1, len2paths.keys()))[0]
print('Part 2: ', ''.join(list(map(lambda x:x[0],len2paths[key][0].split(',')))))

# Part 3

f = open('06.03.input', "r")
input = f.read()
lines = input.split('\n')

tree = {}

for line in lines:
  root = line.split(':')[0]
  branches = line.split(':')[1].split(',')
  tree[root] = branches

paths = traverseTree(tree, 'RR', 'RR', [], ',')

len2paths = {}
for path in paths:
  if len(path) in len2paths.keys():
    len2paths[len(path)].append(path)
  else:
    len2paths[len(path)]=[path]

key = list(filter(lambda x: len(len2paths[x])==1, len2paths.keys()))[0]
print('Part 3: ', ''.join(list(map(lambda x:x[0],len2paths[key][0].split(',')))))