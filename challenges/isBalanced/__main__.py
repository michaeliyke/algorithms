"""
opened is an empty stack
Mark state as valid false
If given symbols set is an odd number, return early
Loop through symbols creating an object of each
when encounter an openner, add it to opened stack
when encounter a closer, match it with the topmost openner:
  yes - reduce opened.
  no - quit. Mark state as valid false
At the end of loop, mark state as valid true
"""

# Balanced symbols
b1 = "(((())))"
b2 = "([]{}())"
b3 = "([{}])"
b4 = "([{}])(()()())[({()})]"

# Unbalanced symbols
u1 = "()((((([{]))))(){[()]}"
u2 = "()((((([]))))(){[()]}"
u3 = "[}([){]"

from challenge import isBalanced
print("\n# Balanced symbols")
print("  symbols: ", b1, "isBalanced: ", isBalanced(b1))
print("  symbols: ", b2, "isBalanced: ", isBalanced(b2))
print("  symbols: ", b3, "isBalanced: ", isBalanced(b3))
print("  symbols: ", b4, "isBalanced: ", isBalanced(b4))
print("\n")

print("\n# Unbalanced symbols")
print("  symbols: ", u1, "isBalanced: ", isBalanced(u1))
print("  symbols: ", u2, "isBalanced: ", isBalanced(u2))
print("  symbols: ", u3, "isBalanced: ", isBalanced(u3))
