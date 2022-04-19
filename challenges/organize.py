import subprocess
import os
import pathlib


CATEGORIES = {
  "DOCUMENTS": [".pdf", ".rtf", ".txt"],
  "AUDIO": [".m4a", ".m4b", ".mp3"],
  "VIDEOS": [".mov", ".avi", ".mp4"],
  "IMAGES": [".jpg", ".jpeg", ".png"],
}

def pickDirectory(file_type):
  for category, suffixes in CATEGORIES.items():
    for suffix in suffixes:
      if file_type == suffix:
        return category
  return "MISC"

def organizeDirectory():
  for f in os.scandir(): # For all things in a directory
    if f.is_dir(): continue # Skip directories
    fp = pathlib.Path(f) # Make a path of the string
    suffix = fp.suffix.lower() # Get the file extension
    directory = pickDirectory(suffix) # Get a directory string
    directoryPath = pathlib.Path(directory) # Make a path of the string
    if not directoryPath.is_dir(): directoryPath.mkdir() # Ensure dir
    fp.rename(directoryPath.joinpath(fp)) # Rename action 

def runPyScript(script):
  # Interrogate the string for a valiid python script
  directoryPath = pathlib.Path(script) # Make a path of the string
  if not directoryPath.is_file(): exit("This script does not exist")
  if  directoryPath.suffix.lower() != ".py": exit("Invalid file")
  subprocess.check_call(["python", directoryPath])
