
"""indexing
Example r = [ [[1,2,3],2,[1,3]],     [1,2,3]]
  index(r, 2)
  [0][0][1]
  [0][1]
  [1][1]
  => [[0,0,1], [0,1], [1, 1]]
"""

indices_list, trace, depth, level = [], [], 0, 0

def indexer(array, value, depth=0, level=0):
  global trace
  
  if depth > 0: trace.append(level)
  for pos, item in enumerate(array):
    level = pos
    if isinstance(item, list):
      # trace = [pos]
      depth += 1
      indexer(item, value, depth, level)
      depth -= 1
    if item != value: continue
    indices_list.append(trace[::])
    indices_list[-1].append(pos)
  trace = []
  return indices_list

def index(array, value):
  return indexer(array, value)

def index_(array, value):
  depth = 0
  for pos, item in enumerate(array): 
    if item != value: continue
    indices_list.append([pos])
  return indices_list

