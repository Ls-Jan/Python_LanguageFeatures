
#6、global关键词声明的变量将位于全局变量域中，否则会在局部变量域中


def Func_1():
    x=1
    print('1、',x,locals())#未声明global的变量将处于局部变量域中

def Func_2():
    global x
    x=2
    print('2、',x,locals())

    
x=0
print('0、',x,'\n')

Func_1()
print('0、',x,'\n')

Func_2()
print('0、',x,'\n')


    











from os import system
system("echo 【按任意键以结束】 & pause>nul")



