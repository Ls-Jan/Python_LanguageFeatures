


import os
import sys

try:
    path1=os.path.split(__file__)[0]#当前文件所在目录
    path2=os.path.join(path1,'..',os.path.split(path1)[1])
    path3=os.path.join(path2,'A')
    path4=os.path.join(path1,'..')
    sys.path.append(path3)#【对应 import trigger】
    sys.path.append(path4)#【对应 import Test6.A.trigger】
    [print(path) for path in sys.path]#输出一下路径
    print()
    import A.trigger
    import trigger
    import Test6.A.trigger
    
except Exception as e:
    print(e)

os.system('pause')
























