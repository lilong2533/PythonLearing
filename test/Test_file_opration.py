#-*- coding:UTF-8 -*-
import os
import ConfigParser

def test1():
    f = open('D:\\03.txt','r')
    while True:
#         content = f.read(5)
#         content = f.readline()
        content = f.next()
        if content :
            print content
#             print content ,'<<<<<<<<< ' ,f.tell()
        else:
            break
    print '------------- end'
    f.close()

def test2():
    f = open('D:\\02.txt' ,'r')
    fo = open('D:\\04.txt' ,'w')
    lines = f.readlines()
    for line in lines:
        print line
        fo.write(line)
#     fo.writelines(lines)
test2()
  
  
# print os.path.abspath('.')
# print 'D:\\Android\\1.AndroidProject 的父目录是：',os.path.dirname('D:\\Android\\1.AndroidProject')
# print 'D:\\Android\\1.AndroidProject 是否是目录：' ,os.path.isdir('D:\\Android\\1.AndroidProject')
# print 'D:\\02.txt 文件的大小是：' ,os.path.getsize('D:\\02.txt')
# print os.path.isfile('D:\\02.txt')
# print os.path.exists('D:\\02.txt')
# print os.path.getatime('D:\\02.txt'),' : ' ,os.path.getctime('D:\\02.txt'),' : ' ,os.path.getmtime('D:\\02.txt')
# print os.path.splitext('D:\\02.txt')

# parser = ConfigParser.ConfigParser()
# parser.read("D:\\lilong_test.ini")
# ini_sections = parser.sections();
# for i_s in ini_sections:
#     print parser.items(i_s)

# for root ,dirs ,files in os.walk("C:\\Users\\lilong\\Downloads"):
#     for file in files:
#         print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<< ' ,file
#         print os.path.join(file)



