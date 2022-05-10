
#4、每次进入新调用时，其对应的locals()都是全新的


def Func():
    print(locals().get('a'))
    a=10
    print(locals().get('a'),'\n')

Func()
Func()
Func()
Func()
Func()





















from os import system
system("echo 【按任意键以结束】 & pause>nul")



