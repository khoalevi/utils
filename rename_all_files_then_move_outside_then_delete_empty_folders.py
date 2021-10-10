import os
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dir", type=str, default="./",
                help="path to desire directory")
ap.add_argument("-n", "--name", type=str, default="",
                help="universal name for files")
args = vars(ap.parse_args())

python_filename = os.path.basename(__file__)

index = 0
for dir, _, filenames in os.walk(args["dir"]):
    for filename in filenames:
        if filename == python_filename:
            continue

        _, ext = os.path.splitext(filename)
        new_filename = args["name"] + str(index) + ext

        src = os.path.join(dir, filename)
        dst = os.path.join(args["dir"], new_filename)
        
        os.rename(src, dst)
        index += 1

for item in os.listdir(os.getcwd()):
    if os.path.isdir(item):
        if not os.listdir(item):
            os.removedirs(os.path.join(os.getcwd(), item))