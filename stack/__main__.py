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
print(isBalanced(b1))
print(isBalanced(b2))
print(isBalanced(b3))
print(isBalanced(b4))
print("\n")

print("\n# Unbalanced symbols")
print(isBalanced(u1))
print(isBalanced(u2))
print(isBalanced(u3))

"""
st is a stack of items (each item is an object with necessary informtion)
st2 is an empty stack
feed char into st2 one at a time moving it from st
when encounter a closer, stop!
Check closed status backward until an unclosed match item is found
If the item is a matching openning, mark its status as closed
if item is not a correct match, stop and match the stack's valid state as false
Continue receiving items
"""
"""
opened is an empty stack
Loop through symbols creating each an object of each
when encounter an openner, add it to opned stack, mark state as valid false
when encounter a closer, match it with the topmost:
  yes - reduce opened.
  no - quit. Valid is already false
In the end, mark state valid as true
"""
"""
DURING push()
MAKE A SEPARATE STACK FOR OPENED
when encounter an openner stop
add it to the opened stack

MAKE A SEPARATE STACK FOR CLOSED
when encounter closer stop!
check if it matches the topmost opened
yes - reduce opened and quit
no - mark list validity as false and quit
"""