uhuntu:apt-get install python
centos:yum install python

the first python demo:1.py


#!/user/bin/python
import os,sys
def calcs(first,sec,third):
        result = first + sec + third
        print result
def main():
        file = "./1.txt"
        f = open(file,'r')
        str = f.readlines()
        str2 = str[2].split(':')[0]
        str3 = str[2].split(':')[1]
        print 'str2 :' + str2 + '\n' + 'str3：‘ + str3
if_name_ == '_main_':
        main()


import sys        import os      类似于c中的include头文件

Data types:
1 代码格式对齐，保持统一缩进格式
2 一行多个语句，分号分割
3 反斜杠\,扩展到下一行
4 关键字
function type() to check the type of the data

in Terminal:
>>>str = 'hello,word'
>>>str
'hello,woed'
>>>str[2:]
'llo,word'

[注意左开右闭] [a,b)  a=<result<b


        
