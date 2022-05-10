

#5、获取locals()的字典后其内容不会同步更新

def Func():
    d=locals()
    a,b,c=(1,2,3)
    print(d)
    print(locals())
    print(d,'\n')#也就是d的内容在调用locals()后才会刷新
    
    d['a']=1000#既然知道不会同步更新的话，那么也就明白对d的操作仅是“隔靴挠痒”白费劲
    print(d)
    print(locals())
    print(d,'\n')

Func()










from os import system
system("echo 【按任意键以结束】 & pause>nul")



