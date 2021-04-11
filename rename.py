import os

for f in os.listdir():
    if '"' in f:
        ff = f.replace('"','')
        os.rename(f, ff)


