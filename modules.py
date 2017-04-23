# how to structure a python program

# one main top level file, and zero or more supplemental files

import something

# imports give access to everything top level

# how imports work

# first find the module's file, ocmpile it to byte code, run the the module's code to build the objects it defines


# compilation process. if there's a .pyc file, then don't recompile

# MODULE SEARCH PATH

# 1. The home directory of the program
# 2. PYTHONPATH directories (if set)
# you can set pythonpath directories s

# 3. Standard library directories
# 4. The contents of any .pth files (if present)
# 5. The site-packages home of third-party extensions

import sys
print sys.path

# ['', 'C:\\code', 'C:\\Windows\\system32\\python33.zip', 'C:\\Python33\\DLLs',
'C:\\Python33\\lib', 'C:\\Python33', 'C:\\Users\\mark',
'C:\\Python33\\lib\\site-packages']

# python loads the direcory in the left most path of sys.path

from module1 import printer

# ^^^ don't have to import evertyhing

# NAMESPACES

# files generate namespaces

# python loads up modules initially, and then once loaded, the top elvel funcs don't do anything

reload(module) #this reloads the the module

import dir1.dir2.mod

# imports a path

# INIT.PY files
#
# package initialization file. serves as a hook for packages
# rusn all the code in the __init__.py file great place to put initialization stuff
# tell that a directory is a python package
# creates the name space

from . import names



