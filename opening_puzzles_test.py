# import required module
import os
# assign directory
directory = r"C:\Users\Zbook\Downloads\opening data"
 
# iterate over files in
# that directory
puzzles_number = 0
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        with  open(f, "r") as f:
            puzzles_number += len(f.read().split("\n\n["))
print(puzzles_number)