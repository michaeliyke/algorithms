

class Symbol:
  def __init__(self, symbol: str) -> None:
    self.symbol = symbol
    self.closer = ""
    if symbol == "{":
      self.closer = "}"

    if symbol == "[":
      self.closer = "]"

    if symbol == "(":
      self.closer = ")"

  def __str__(self) -> str:
      return self.symbol
  
  def isACloser(self) -> bool:
    return len(self.closer) == 0


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
    return "".join([str(x) for x in self.list])


class Balancer:
  def __str__(self) -> str:
      return str(self.opened)

  def isBalanced(self) -> bool:
    return self.valid
  
  def feed(self, symbols) -> bool:
    opened = Stack()
    self.valid = False

    if len(symbols) % 2 == 1: return self.valid

    for s in symbols:
      symbol = Symbol(s)
      if not symbol.isACloser():
        opened.push(symbol)
        continue

      openner: Symbol = opened.pop()
      if symbol.symbol != openner.closer:
        self.valid = False
        break

      self.valid = True

    return self.valid
      
