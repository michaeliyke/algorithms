import os
from pathlib import Path
import pathlib
import re
import time


def books(folder, dest):
  path = folder if isinstance(folder, Path) else Path(folder)
  dest = Path(dest)
  destName = dest.name
  if dest.name =="*": destName = ""
  reg = re.compile(r"[\W_]+{}[\W_]+".format(destName), re.IGNORECASE)
  for item in os.scandir(path):
    newpath = "{}\{}".format(
      str(dest)[:-2] if dest.name == "*" else dest , item.name,
      )
    item = Path(item)
    # print( item.name if item.is_dir() else item.name)
    if item.suffix.lower() == ".pdf" and reg.search(item.name):
      print("\n Moving\n {}\n ...".format(item))
      time.sleep(3)
      # print(item.name, ":\n", newpath)
      os.rename(item, newpath)
    if item.is_dir():
      books(item, dest)
