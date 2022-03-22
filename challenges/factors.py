def pf(number):
  divisor = 2; 
  while(number > 1):
    if number % divisor == 0: 
      number = number / divisor
      yield divisor 
      continue
    divisor += 1

def f(number):
  divisor = 0; 
  while(divisor < number):
    divisor += 1
    if number % divisor == 0: yield divisor

# Prime number - divisible only by 1 and itself
# Prime factor - A factor that is a prime number
def primesOf(number):
  """factorsOf takes an integer x 

  returns a list containing all of its prime factors
  
  f(630) - [2, 3, 3, 5, 7] - 2*3*3*5*7 - 630
  f(13) - [13]
  """
  return list(pf(number))

def of(number):
  return list(f(number))