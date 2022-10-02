 import sys
import os
import json


with open("tokens.txt", "a+")as f:
  pass
with open("tokens.txt", "r")as f:
  tokens = f.readlines()
for token in tokens:
  mail, password, token = str(token).strip().split(":")
  with open("tokensconverted.txt", "a+")as f:
    f.write(token + "\n")