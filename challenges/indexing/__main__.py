import indexing, solution
# An array of tupples - (InputArray, ExpectedOuput)
items = [
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
    [[1], [2, 0, 2], [2, 0, 4, 0], [2, 0, 4, 1, 0], [2, 0, 4, 1, 1, 0], [2, 0, 4, 1, 1, 1, 0], [2, 0, 4, 1, 1, 1, 1, 0], [2, 0, 4, 1, 1, 1, 1, 1, 0], [2, 0, 4, 1, 1, 2], [2, 0, 4, 2], [2, 1]],
  ),
  (
    [0, 3, [[ 9, 5, 3, 0, [3, [3, [3, [3, [3, [3] ], 1], 2], 1], 2]], 2]],
    [[2, 0, 4, 1, 1, 2], [2, 0, 4, 2], [2, 1]],
  ),
]

for item in items:
  inputArray, expectedOutput = item
  # output = indexing.index(inputArray, 2)
  output = solution.index(inputArray, 2)
  print("\n  Input: ", inputArray)
  print("  Outputed: ", output)
  print("  Expected: ", expectedOutput)
  print("  Indexing passed: %s \n" % (expectedOutput == output))