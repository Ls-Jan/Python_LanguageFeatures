
#7、可以对globals()进行直接修改以影响全局变量，和global声明变量差不多的效果，只不过使用globals()甚至可以直接删掉全局变量
#globals()和locals()完全不同，locals()简直就是个废的，根本不能拿locals()做些什么建设性的操作


def Func_1():
    globals()['x']=1
    print('1、',x)

def Func_2():
    globals().pop('x')#删掉全局变量x
    try:#因为x不存在所以用异常捕捉
        print('2、',x)
    except Exception as e:
        print('！2、',e)

Func_1()
print('0、',x,'\n')
Func_2()

try:#因为x不存在所以用异常捕捉
    print('0、',x)
except Exception as e:
    print('！0、',e)
    











from os import system
system("echo 【按任意键以结束】 & pause>nul")



