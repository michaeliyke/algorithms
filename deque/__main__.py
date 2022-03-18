"""
Loop thro and add ch to rear of deck for constant time
As long as d's size >= 2, remove front-most and rear-most item into their vars
If those variables aren't equivalent, return early
If the variables are the same, proceed to the next items
If the size of the deck eventually gets to be smaller than 2, return true
"""

from palidrome import show_palindrome
  
palindromes = [
  "B",
  "AA",
  "kayak",
  "civic",
  "radar",
  "rotor",
  "noon",
  "Nurses run.",
  "Madam, I'm Adam.",
  "Eva, can I stab bats in a cave?",
  "Madam in Eden, I'm Adam.",
  "Mr. Owl Ate My Metal Worm.",
  "A Santa Lived as a Devil At NASA.",
  "Dammit, I'm mad!",
  "Was it a rat I saw?",
  "Do Geese see God?",
  "Never odd or even!",
  "A Man, A Plan, A Canal-Panama!",
]

show_palindrome(palindromes)