#-*- coding:UTF-8 -*-
import os

# ekeys = os.environ.keys()
# for item in ekeys:
#     if 'PATH' == item:
#         p_item = os.environ.get(item)
#         print p_item

print os.path.abspath('.')
import subprocess
import signal


# def signal_handler(signum, frame):
#     print '+++++++++++++++++++++ ' ,signum , ' : ' ,frame
#     
# signal.signal(signal.SIGINT, signal_handler)
# 
# pingP = subprocess.Popen(args = 'ping -n 4 www.baidu.com' ,shell = True ,cwd = 'D:\\') 
# pingP.wait()
# print pingP.stdout.read()

print '--------------'
f = open('D:\\sp.txt','w+')
try:
    ret = subprocess.check_call('exit 1',shell = True)
    print '--------------'
    print ret
except subprocess.CalledProcessError ,e:
    print '-------------- : ',e.returncode
    

