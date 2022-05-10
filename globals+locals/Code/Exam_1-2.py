
#2、locals()返回局部变量，在不同地方是不同的东西

def Func():
    a,b,c,d,e=[0]*5
    print(locals(),'\n')

Func()
print(locals(),'\n')























from os import system
system("echo 【按任意键以结束】 & pause>nul")
