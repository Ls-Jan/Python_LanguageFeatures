
#1、如果exec不传入字典的话将会默认传入globals()和locals()


def Func(order:str):
    print('G：',list(globals().keys()))
    print('L：',list(locals().keys()))
    print()

    exec(order)

    print('G：',list(globals().keys()))
    print('L：',list(locals().keys()))
    print()

Func('a=1')

















from os import system
system("echo 【按任意键以结束】 & pause>nul")
