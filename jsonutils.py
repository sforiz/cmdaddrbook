import json

def python2jsonfile(dict, filename, filemode="w"):
  f = open(filename, filemode)
  json.dump(dict, f, indent=2, separators=(',', ':'))
  f.close()
  del f

def jsonfile2python(filename, filemode="r"):
  f = open(filename, filemode)
  return json.load(f)
  f.close()
  del f