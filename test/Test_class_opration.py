from utils import myclasses
import gc

# shop = myclasses.FruitShop('lilong_shop')
# print shop.name

###############################################################
class AName(object):
     
    def __new__(cls ,*args ,**cwd):
        print '__new__ : cls = ',cls
        print '__new__ : args = ',args
        print '__new__ : cwd = ',cwd
        return object.__new__(cls,args ,cwd)
         
    def __init__(self,*args ,**cwd):
        print '__init__ : self = ',self
        self.name = 'lilong'
        
    def __str__(self):
        return 'AName'
    
    def __call__(self):
        print 'AName : __call__'
        
aname = AName('lilong','zhangsan','wangwu',a = 'lilong',b = 'zhangsan',c = 'wangwu')
# aname();
# print isinstance(aname, object)
# print '================================'
# aname = AName('lilong','zhangsan','wangwu',a = 'lilong',b = 'zhangsan',c = 'wangwu')

print aname.name
