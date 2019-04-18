import os

try:
  os.mkdir('temp')
except FileExistsError:
  pass