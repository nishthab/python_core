#import common_util
#import common_util as common
from moduels.common_util import  *
import subprocess
import sys
import os

'''
Form where the module is getting 
It has three level 
1. is current directory
If It is not found it will go to the library path python installable
IF you want to check in the user define library. There is a environmental variable called PYTHONPATH
'''
# Invoke the function
print("-------------------------------------------")
#print(common.chk_mailId("nishtha.bhardwaj@gmail.com"))
#print(common.welcome_user("Nishtha"))
print(chk_mailId("nishtha.bhardwaj@gmail.com"))
print(welcome_user("Nishtha"))
print("-------------------------------------------")

# sys module
#sys.exit()
print("Version of Python:-", sys.version)
print("Version of Python:-", sys.version_info)
print("commond line argument->",sys.argv)
print( sys.exc_info())

print("----------------------------------------------")

# os module
print("-----------------------------------------------")
dir_name = os.getcwd()
print("Current working directory-",dir_name)

#os.path
print(os.path.join(dir_name,sys.argv[0]))
print(os.path.abspath(sys.argv[0]))

fullpath = os.path.join(dir_name,sys.argv[0])
"""dir1/dir2/filename.txt dir1/dir2 - directory name and filename.txt is base name 
if you have dir1/dir2 then dir2 is a
 base name and rest all will be considered as directory name
 ('C:/Users/nbhardwaj/workspace/test', 'call_utils.py')
 C:/Users/nbhardwaj/workspace/test' - dir name
 'call_utils.py' - base name
 
 """
print(os.path.split(fullpath))
print("-----------------------------------------------")
# to run the
print(subprocess.call('dir' ,shell=True))
print("------------------------------------------------")