

#5、返回的locals()中可以出现解释器中不存在的变量(但这没有一点意义


def Func():
    d=locals()
    d['xxx']=0
    print(d)
    print(locals())#只不过很可笑的一点是，它不会删除解释器中不存在的变量(也就是xxx压根是不存在的，但它没将其移除)
    print(d,'\n')
    try:
        print(xxx)
    except Exception as e:
        print(e)



Func()





from os import system
system("echo 【按任意键以结束】 & pause>nul")



