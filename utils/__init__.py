#-*- coding:UTF-8 -*-
if __name__ == '__main__':
    print ''' com.lenovo.utils 作为主程序运行 '''
else:
    print ''' com.lenovo.utils 初始化 '''
    
#这里将tools模块添加进入com.lenovo.utils包，其他模块就可以
#通过"from com.lenovo.utils inport *"引入utils包来访问到tools模块
__all__ = ["tools" ,"myclasses"]

