"""Create a function that takes in a string of symbol pairs as parameter.

The function should return true if the symbol string is balanced 
or false if not.

For symbols to be balanced, each opening symbol should also have a 
closing symbol, and the symbols must be properly nested.

Make use of a stack in your solution

Balanced symbols
([{}])
([]{}())
(((())))

Unbalanced symbols
(([{])
[}([){]
"""

from stack import Balancer

def isBalanced(symbols):
  balancer = Balancer()
  balancer.fill(symbols)
  # print(balancer)
  return balancer.isBalanced()