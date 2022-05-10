
#2、如果exec传入字典一个字典的话那么会作为全局和本地变量使用
#即，在exec中定义的变量将保存到这个字典中

def Func_1(order:str):
    print('G：',list(globals().keys()))
    print('L：',list(locals().keys()))
    print()

    exec(order,globals())

    print('G：',list(globals().keys()))
    print('L：',list(locals().keys()))
    print()
    
def Func_2(order:str):
    print('G：',list(globals().keys()))
    print('L：',list(locals().keys()))
    print()

    exec(order,locals())

    print('G：',list(globals().keys()))
    print('L：',list(locals().keys()))
    print()

def Func_3(order:str):
    d=dict()

    print('G：',list(globals().keys()))
    print('L：',list(locals().keys()))
    print('D：',list(d.keys()))
    print()
    
    exec(order,d)

    print('G：',list(globals().keys()))
    print('L：',list(locals().keys()))
    print('D：',list(d.keys()))
    print()

Func_1('a=1')
Func_2('b=1')
Func_3('c=1')




