import os

path = os.getcwd()
parent = os.path.abspath(os.path.join(path, os.pardir))

dirs = []
for root,dir,files in os.walk(parent):
    dirs.append(root)

DBPATH = os.path.join(dirs[-2],"Medicine.sqlite3")
