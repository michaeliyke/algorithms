import time, random


def waitGame():
  target = random.randint(2, 4)
  print("\n Your target time is {} seconds".format(target))
  input(" ---Press Enter to Begin---")
  start = time.perf_counter()
  input("\n ...Press Enter again after {} seconds...".format(target))
  elapsed = time.perf_counter() - start
  print(" Elapsed time: {:.3f} seconds".format(elapsed)) 
  if (elapsed == target):
    print(" Unbelievable! Perfect timing!")
  if (elapsed < target):
    print(" {0:.3f} seconds too fast".format(target - elapsed))
  if (elapsed > target):
    print(" {0:.3f} seconds late".format(elapsed - target))