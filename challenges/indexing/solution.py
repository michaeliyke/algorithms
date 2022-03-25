# This is the provided solution for the challenge
# - Great lesson - 
# Result of a recursion can be utilized within the function
# Original
def index(search_list, item):
  indices = list()
  for i in range(len(search_list)):
    if search_list[i] == item:
      indices.append([i])
    elif isinstance(search_list[i], list):
      for indx in index(search_list[i], item):
        indices.append([i]+indx)
  return indices

# Modied
def index(search_list, item):
  def indexer(search_list, item):
    for i in range(len(search_list)):
      if search_list[i] == item:
        yield [i]
      elif isinstance(search_list[i], list):
        for indx in indexer(search_list[i], item):
          yield [i]+indx
  return list(indexer(search_list, item))