
"""indexing
Example r = [ [[1,2,3],2,[1,3]],     [1,2,3]]
  index(r, 2)
  [0][0][1]
  [0][1]
  [1][1]
  => [[0,0,1], [0,1], [1, 1]]
"""
def index(array, value):
  
  indices_list, trace, depth, level = [], [], 0, 0

  def indexer(array, value, depth=0, level=0):
    nonlocal trace
    # if depth > 0: trace.append(level)
    for pos, item in enumerate(array):
      level = pos
      if isinstance(item, list):
        depth += 1
        if depth > 0: trace.append(level)
        indexer(item, value, depth, level)
        depth -= 1
        trace.pop()
        continue
      if item != value: continue
      # if depth > 0 and tace == []: trace.append(level)
      indices_list.append(trace[::])
      indices_list[-1].append(pos)
    # trace = []
    return indices_list

  return indexer(array, value)
