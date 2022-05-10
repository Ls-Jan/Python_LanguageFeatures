

#5、id(locals())变化理由不明

def Func_1():
    d=locals()
    print(id(locals()))

def Func_2():
    print(id(locals()))

    

Func_1()
Func_1()
Func_1()
Func_1()
Func_1()

print()

Func_2()
Func_2()
Func_2()
Func_2()
Func_2()











from os import system
system("echo 【按任意键以结束】 & pause>nul")



