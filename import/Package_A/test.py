
# for key in dir():
    # print(key,"：",eval(key))
# print("test————————————————————————————————")


from XJImporter import XJImporter
Import = XJImporter(globals()).Import
print(">>>",XJImporter)
Import('../func','*')


class test:
    def __init__(self,num):
        self.__num=num
    def GetVal(self):
        return func(self.__num,self.__num)



if __name__=='__main__':
    t=test(10)
    print(t.GetVal())
