import os
cpt = sum([len(files) for r, d, files in os.walk("./")])

print(cpt)