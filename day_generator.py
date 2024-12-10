#!/usr/bin/python3
import os
import shutil

start = 2

end = 25

for i in range(start + 1, end + 1):
    os.makedirs(f"Day_{i}")
    shutil.copy("Day_2/Day_2.py", f"Day_{i}/Day_{i}.py")
    shutil.copy("Day_2/Day_2_input.txt", f"Day_{i}/Day_{i}_input.txt")
