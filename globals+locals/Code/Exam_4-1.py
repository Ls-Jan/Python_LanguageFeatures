
#4、locals()和它当前所处的递归调用栈的深度直接相关

def Func_1():
    print(id(locals()),id(globals()))

def Func_2():
    print(id(locals()),id(globals()))

Func_1()
Func_2()
print(id(locals()),id(globals()),'\n')



















from os import system
system("echo 【按任意键以结束】 & pause>nul")



