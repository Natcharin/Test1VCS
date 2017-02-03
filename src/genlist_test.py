#! Insert the current directory path to Python Path
import sys
import os
cwd = os.getcwd()#Current Working directory

sys.path.append(cwd)
#print(sys.path)

#Test the module: generate_list
from generate_list import printIT
for i in range(0, 1000):
    printIT()