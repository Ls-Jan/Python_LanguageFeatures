
#4、函数内使用exec的话建议传入指定字典，用于记录以及使用变量

class Test:
    def __init__(self):
        self.__valDict=dict()

    def exec_1(self,order):
        exec(order,self.__valDict)

    def exec_2(self,order):
        try:
            exec(order)#这里不传入字典，所以在执行print(b)时会报错
        except Exception as e:
            print(e)
            
            
            
t=Test()
t.exec_1("a=1")
t.exec_1("print(a)")

t.exec_2("b=2")
t.exec_2("print(b)")










from os import system
system("echo 【按任意键以结束】 & pause>nul")
