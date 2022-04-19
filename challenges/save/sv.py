import pickle
from typing import Dict


def saveDict(dictionary: dict, file_path: str):
  txt = ""
  for k, v in dictionary.items():
    txt += "{} = {}\n\r".format(k, v)
  
  file_save(txt, file_path)

def file_save(txt: str, file_path: str):
  with open(file=file_path, mode="w") as file:
    file.write(txt)

def read_file(file_path: str) -> str:
  txt: str = ""
  with open(file=file_path, mode="r") as file:
    for line in file.readlines():
      txt += line + "\n\r"
  return txt

def pickeSaveDict(dictionary: dict, file_path: str):
  with open(file=file_path, mode="wb") as f:
    pickle.dump(dictionary, f)

def pickeReadDict(file_path: str) -> dict:
  with open(file=file_path, mode="rb") as f:
    return pickle.load(f)

def readDict(file_path: str) -> dict:
  txt, d = read_file(file_path), dict()
  for line in txt.split("\n\r"): 
    if len(line.split()) < 2: continue
    [left, right] = line.split("=")
    d[left.strip()] = right.strip()
  
  return d
