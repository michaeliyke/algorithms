
from typing_extensions import Self


class Symbol:
  def __init__(self, symbol: str) -> None:
    self.symbol = symbol
    self.closer: str
    self.openner: str
    if symbol == "{":
      self.closer = "}"

    if symbol == "}":
      self.openner = "{"

    if symbol == "[":
      self.closer = "]"

    if symbol == "]":
      self.openner = "["

    if symbol == "(":
      self.closer = ")"

    if symbol == ")":
      self.openner = "("

    self.closed = False

  def __str__(self) -> str:
      return self.symbol


class Stack:

  def __init__(self):
    self.list = []
  
  def push(self, item):
    """Appends item to the end of list. Returns nothing.

    Runtime is O(1) since list append happens in constant time"""
    self.list.append(Symbol(str(item)))
  
  def pop(self):
    """Removes and returns the topmost item on the list
    
    Runtime is O(1) removing the topmost item happens in constant time"""
    if not self.is_empty():
      return self.list.pop()
  
  def peek(self):
    """Returns the tompost item on the list
    
    Runtime is O(1) since indexing into list happens in constant time"""
    if not self.is_empty():
      return self.list[-1]
  
  def is_empty(self) -> bool:
    """Returns a boolean value showing whether or not the list is empty
    
    Runtime is O(1) since testing for equality happens in constnt time"""
    return self.size() == 0
  
  def size(self) -> int:
    """Returns the number of items on the list
    
    Runtime is O(1) since finding the size of a list happens in constant time"""
    return len(self.list)
  
  def __str__(self) -> str:
    return str([str(x) for x in self.list])


class StackWrapper:

  def checkSymbol(self, wrapper: Self, closing: str) -> None:
    while not wrapper.stack.is_empty:
      symbol: Symbol = wrapper.stack.pop()
      if symbol.closer == closing:
        symbol.closed = True
        break

  def __str__(self) -> str:
      return str(self.stack)
  
  def __init__(self):
    self.stack = Stack()
    self.valid = True

  def push(self, item: Symbol, wrapper: Self):
    if not self.valid:
      return

    if item.symbol == "}" or item.symbol == "]" or item.symbol == ")":
      print("This is a closer", item.openner, item.symbol)
      self.valid = self.checkSymbol(wrapper)
      pass
    return self.stack.push(item)


class Balancer:
  def __str__(self) -> str:
      return str(self.stack)
      
  def __init__(self):
      self.wrapper = StackWrapper()
      self.stack = self.wrapper.stack
  
  def isBalanced(self) -> bool:
    wrapper = StackWrapper()
    while not self.stack.is_empty() and self.wrapper.valid:
      wrapper.push(self.stack.pop(), wrapper)
    print(self.stack, ":", wrapper)
    return False
  
  def feed(self):
    return self.wrapper.valid # For isBalanced
  
  def fill(self, symbols):
    it = 0
    self.symbols = symbols
    while it < len(symbols):
      s = symbols[it]
      it += 1
      if self.stack.push(Symbol(s)):
        break
