from importlib.resources import path
import sv

dic = {
  "Name": "Michael C. Iyke",
  "Age": 33,
  "Occupation": "Software Engineering",
  "Location": "Lagos, Nigeria",
  "Complexion": "Light",
  "Religion": "Christianity",
  "Interests": "Philosophy, Science, Technology",
  "Espoused": False
}

file_path = "./saved.pickle"

# sv.pickeSaveDict(dic, file_path)
print(sv.pickeReadDict(file_path))