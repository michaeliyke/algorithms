import indexing

items = [
  # input => result maps
  (
    [1,2,3, 2, 5, 1, 1, 2, 0, 2, 5],
    [[1], [3], [7], [9]],
  ),
  (
    [3, 2, 5, 1, 1, [2, 0, 2,1, 2, [3,2]], 2, 5], 
    [[1],[5,0],[5,2],[5,4],[5,5,1], [6]],
  ),
  (
    [2, [2, [2, [2, [2, [2] ]]]]], 
    [[0],[1,0],[1,1,0],[1,1,1,0], [1,1,1,1,0],[1,1,1,1,1,0]],
  ),
  (
    [ [[1,2,3],2,[1,3]],[1,2,3]], 
    [[0, 0, 1], [0, 1], [1, 1]],
  ),
  (
    [0, 2, [[ 9, 5, 2, 0, [2, [2, [2, [2, [2, [2] ], 1], 2], 1], 2]], 2]],
    [[1], [2,0,2], [2,0,4,0], [2,0,4,1,0], [2,0,4,1,1,0], [2,0,4,1,1,1,0], 
    [2,0,4,1,1,1,1,0], [2,0,4,1,1,1,1,1,0],  [2,1]]
  ),
  (
    [0, 3, [[ 9, 5, 3, 0, [3, [3, [3, [3, [3, [3] ], 1], 2], 1], 2]], 2]],
    [[2, 0, 4, 1, 1, 2], [2, 0, 4, 2], [2, 1]],
  ),
]

# l = [1,2,3, 2, 5, 1, 1, 2, 0, 2, 5]
# print(indexing.index(l, 2))
# print([[1], [3], [7], [9]])
# 
# l = [3, 2, 5, 1, 1, [2, 0, 2,1, 2, [3,2]], 2, 5]
# print(indexing.index(l, 2))
# print([[1],[5,0],[5,2],[5,4],[5,5,1], [6]])
# 
# l = [2, [2, [2, [2, [2, [2] ]]]]  ]
# print(indexing.index(l, 2))
# print([[0],[1,0],[1,1,0],[1,1,1,0], [1,1,1,1,0],[1,1,1,1,1,0]])
# 
# l = [ [[1,2,3],2,[1,3]],     [1,2,3]]
# print(indexing.index(l, 2))
# print([[0, 0, 1], [0, 1], [1, 1]])

for item in items:
  inputArray, expectedResult = item
  output = indexing.index(inputArray, 2)
  print("Input: ", inputArray)
  print("Output: ", output)
  print("Expected: ", expectedResult)
  print("Indexing passed: %s \n" % (expectedResult == output))
  # Could you believe bro that I have been struggling to get this algorithm right 
  # for three days. Of course I pulled out  
  # Even as it works, I'm still nervous that an input might push it 
  # really hard and it breaks. 
  # All it does is index an input for a given value - in this case, I feed it with an
  # arbitrarily nested array of numbers looking for the number 2. 
  # The job of this algorithm is to return an array with direct lookup locations of all the 2s
  # found in the input.
  # Example:
  # arr = [[3,2], 1, 2]
  # index(arr)
  # return value [[0, 1], [2]]
  # Meaning
  #   arr[0][1] - locates the first 2 in the input
  #   arr[2] - locates the second 2 in the input
  # Of course the input can get urgily:
  [0, 2, [[ 9, 5, 2, 0, [2, [2, [2, [2, [2, [2] ], 1], 2], 1], 2]], 2]],
# [[1], [2,0,2], [2,0,4,0], [2,0,4,1,0], [2,0,4,1,1,0], [2,0,4,1,1,1,0], [2,0,4,1,1,1,1,0], [2,0,4,1,1,1,1,1,0],  [2,1]]
# So, it flattens the array and releases all the occurences of the required value
  # You can check it out on my Github