
from deque import Deque
import re, os

def shifts(s, ch=None):
  if ch == None:
    ch = "-"
  max = 0
  for p in palindromes:
    if(len(p) > max):
      max = len(p)

  n = max - len(s)
  return ch * n

def is_palindrom(s: str):
  s = re.sub(r"[^a-zA-Z]", "", s).lower()
  d = Deque()
  for ch in s:
    d.add_rear(ch)
  
  while(d.size() >= 2):
    if d.remove_rear() != d.remove_front():
      return False

  return True


def is_palindrom2(s: str):
  forwards = "".join(re.findall(r"[a-z]", s.lower()))
  return forwards == forwards[::-1]

def show_palindrome(array):
  os.system("cls")
  if type(array) is not list:
    raise("show_palidrome() required a list of palidromes")
  global palindromes
  palindromes = array
  print("\n\n  ", shifts("-"*24, " ") + "is_palindrome( )".upper(), "\n")
  for p in palindromes:
    print("  '"+p +"'", shifts(p, ":"), is_palindrom(p))


palindromes = []