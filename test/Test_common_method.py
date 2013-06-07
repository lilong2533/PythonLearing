import operator
import glob
import os

# moudles = []
# for item in glob.glob("LibLearing01.py"):
#     moudle ,ext = os.path.splitext(os.path.basename(item))
#     m = __import__(moudle)
#     moudles.append(m)
#     
# for index in moudles:
#     moudles[index].hello()

#------------------------------------------------
namespace = {}
# eval("__import__('os').getcwd()" ,namespace)
print eval("__import__('os').getcwd()" ,{})

#------------------------------------------------
