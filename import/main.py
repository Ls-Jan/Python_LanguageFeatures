# for key in dir():
    # print(key,"：",eval(key))
# print("main————————————————————————————————")

import os

exec('import trigger')
import trigger
os.system('pause')
exit()

os.system('chcp 936')
# import Package_B.trigger2
if __name__=='__main__':
    try:
        import XJImporter
        print(">>>",XJImporter)
        # from Package_B import test
        from Package_A import test
        t=test(100)
        print(t.GetVal())
    except Exception as e:
        print(e)


os.system('pause')
