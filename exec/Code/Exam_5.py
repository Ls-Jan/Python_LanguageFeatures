
#5、exec的解释器可是很乖的，传入exec的局部变量字典和解释器的局部变量严格同步

def Func_1():
    exec("a=1")
    print(locals())
    locals().clear()#把局部变量字典清理一下后，刚刚定义的a就不见了，个腊鸡玩意儿简直气死个人
    print(locals())#说白了就是，别妄想通过locals()来修改局部变量
    
    
def Func_2():
    d1={'a':1}
    d2={'a':2}
    exec('print(a)',d1,d2)#它真的，好乖，我枯死。
    

Func_1()
print('\n\n')
Func_2()





from os import system
system("echo 【按任意键以结束】 & pause>nul")
