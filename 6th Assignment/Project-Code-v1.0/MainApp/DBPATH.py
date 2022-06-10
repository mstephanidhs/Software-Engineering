import os
import re
path = os.getcwd()
parent = os.path.abspath(os.path.join(path, os.pardir))

dirs = []
for root,dir,files in os.walk(parent):
    dirs.append(root)

pattern = re.compile(r"Model$")
for i in dirs:
   if pattern.search(i):
       location = i


DBPATH = os.path.join(location,"Medicine.sqlite3")
