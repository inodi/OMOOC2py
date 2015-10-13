#-*- coding: utf-8 -*-
# Quick Python Script Explanation for Proqeammers
# 给程序猿的超快Py脚本解说

import sys 
reload(sys) 
sys.setdefaultencoding('utf8') 

import os

def main():
    print 'Hello World!'
    print "这是Alice\'的问候。".decode("utf8").encode("gbk")
    print "这是Bob\'的问候。".decode("utf8").encode("gbk")

    foo(5, 10)

    print '=' * 10
    print '这将直接执行'+os.getcwd()
    counter = 0
    counter += 1
  
    food = ['苹果','杏子','李子','梨']
    for i in food:
        print '他就是爱一只：'+i
  
    print '数到10'

    for i in range(10):
        print i
  
def foo(paraml, secondParam):
    res = paraml+secondParam
    print '%s plus %s equal %s'%(paraml,secondParam, res)
    if res < 50:
       print '这个'.decode("utf8").encode("gbk")
    elif (res >= 50) and ((paraml == 42) or (secondParam == 24)):
       print '那个'.decode("utf8").encode("gbk")

    else:
       print '啦啦啦啦啦啦我是卖报的小行家。'.decode("utf8").encode("gbk")

    return res  #老师说这是单行注释
'''老师说这是多行注释，俩都是合法注释……'''
if __name__=='__main__':
    main()

#因为不知道需要写到什么程度，于是从下面开始是我在42行基础上自己写着玩的程序。
print "你走进了一家咖啡馆，招待你的是一只黑色的兔子。".decode("utf8").encode("gbk")

print "你想要哪种咖啡?".decode("utf8").encode("gbk")
print "1.焦糖玛奇朵。".decode("utf8").encode("gbk")
print "2.薄荷拿铁。".decode("utf8").encode("gbk")
print "3.意大利浓缩。".decode("utf8").encode("gbk")
print "4.美式咖啡。".decode("utf8").encode("gbk")

coffee = raw_input ("> ")

if coffee == "1":
    print "黑兔子把耳朵剪下来。".decode("utf8").encode("gbk")
elif coffee == "2":
    print "黑兔子把绿色的眼睛拿了出来。".decode("utf8").encode("gbk")
elif coffee == "3":
    print "黑兔子自己塞进了杯子。".decode("utf8").encode("gbk")
elif coffee == "4":
    print "黑兔子吐出一只白兔子。".decode("utf8").encode("gbk")
else:
     print "黑兔子忽然变成了一只巨大的猴子吃掉了你。".decode("utf8").encode("gbk")
