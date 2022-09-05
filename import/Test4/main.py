


import os
import sys

try:
    path1=os.path.split(__file__)[0]#当前文件所在目录
    path2=os.path.join(path1,'..',os.path.split(path1)[1])#我故意的，故意把路径搞长，便于做出明显的对比
    path3=os.path.join(path2,'A')#包A路径
    sys.path.append(path3)
    [print(path) for path in sys.path]#输出一波路径
    print()
    import A.trigger#【常规导入】
    import trigger#【非常规导入】
except Exception as e:
    print(e)

os.system('pause')
























