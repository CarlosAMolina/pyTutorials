#!/usr/bin/python
__author__ = 'Carlos A. Molina - @CarlosAMoli'

# script that uses functions in different paths

import sys
import os

# path of this script
scriptPath = os.path.dirname(os.path.abspath(__file__))
# path to other functions from this script
path1 = '..'
path2 = '../folder2'
path3 = 'folder3'

# add functions' paths
sys.path.append(scriptPath + '/' + path1)
sys.path.append(scriptPath + '/' + path2)
sys.path.append(scriptPath + '/' + path3)

# import functions
from scriptWithFunction1 import sayHi
from scriptWithFunction2 import sayBye
from scriptWithFunction3 import sayLater

# use functions
sayHi()
print '----'
sayBye()
print '----'
sayLater()
