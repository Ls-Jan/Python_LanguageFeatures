
#4、locals()和它当前所处的递归调用栈的深度直接相关


def Func_1():
    print(id(locals()))
    Func_2()

def Func_2():
    print(id(locals()))
    Func_1()

print(id(locals()),id(globals()))

try:#因为会爆栈，所以异常捕捉
    Func_1()
except Exception as e:
    print(e)


















from os import system
system("echo 【按任意键以结束】 & pause>nul")



