
#3、dir()可以获取局部变量列表

def Func():
    print(list(locals().keys()))
    print(dir(),'\n')

Func()
print(list(locals().keys()))
print(dir(),'\n')



from os import system
system("echo 【按任意键以结束】 & pause>nul")



