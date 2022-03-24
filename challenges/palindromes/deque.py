class Deque:
  """Left side of the list represent the front of the dequeue

  whereas the right side represents the end of the list
  """
  def __init__(self):
    self.items = []
  
  def add_front(self, item):
    """Inserts an item intothe 0th index of the list
    
    Runtime is O(n) or linear time
    """
    self.items.insert(0, item)
  
  def add_rear(self, item):
    """Appends an item to the end of the list
    
    Runtime is O(1) or constant time"""
    self.items.append(item)
  
  def remove_front(self):
    """Remove and return the item on the 0th index on the list
    
    Runtime is O(1) or linear time"""
    if not self.is_empty():
      return self.items.pop(0)
  
  def remove_rear(self):
    """Removes and returns the last item of the list
    
    Runtime is O(1) or constant time"""
    if not self.is_empty():
      return self.items.pop()
  
  def is_empty(self):
    return self.items == []
  
  def peek_front(self):
    """Look up the 0th or first item on the list
    
    Runtime is O(1) or constant"""
    if not self.is_empty():
      return self.items[0]
  
  def peek_rear(self):
    """Look up the last item on the list
    
    Runtime is O(1) or constant"""
    if not self.is_empty():
      return self.items[-1]

  def size(self):
    return len(self.items  )