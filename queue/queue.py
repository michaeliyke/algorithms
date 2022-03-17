class Queue:
  """Queue Implementation - FIFO

    Direction is back-front (left-right)
    Back/Start of list - left-most item
    Front/End of list - right-most item
  """
  def __init__(self) -> None:
    self.items = []
  
  def enqueue(self, item):
    """Inserts item at the 0th index of the list - left-most
    
    Runtime is O(N) or linear time
    """
    self.items.insert(0, item)
  
  def dequeue(self):
    """Removes item at the end of list - right-most
    
    Runtime is O(1) or constant time"""
    if not self.is_empty(): return self.items.pop()
  
  def is_empty(self):
    return len(self.items) == 0
  
  def peek(self):
    """Returns the next item on the list to be dequeued
    
    Runtime is O(1) or constant time"""
    if not self.is_empty(): return self.items[-1]
  
  def size(self):
    """Returns the number of items on the list
    
    Runtime is O(1) or constant time"""
    return len(self.items)