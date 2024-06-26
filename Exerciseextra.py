import os
directory = "/Users/vedantkaushik/Documents/Python/Python"
files = os.listdir(directory)
n = 8
for file in files:
    if file.startswith(f"problem{n}.py"):
      os.rename(os.path.join(directory, f"problem{n}.py"), os.path.join(directory, f"Exercise{n}.py"))
    n += 1
