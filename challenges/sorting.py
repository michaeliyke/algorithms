
# Sort in alphabetical order ignoring casing but return with casing
def sortStr(s: str) ->str:
  return " ".join(sorted(s.split(), key=str.casefold))
