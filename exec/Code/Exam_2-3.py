
#3、如果exec传入两个字典的话这两个字典将依次作为全局变量和局部变量使用

d1=dict()
d2=dict()

exec('a=1',d1,d2)
print(list(d1.keys()),'\n',list(d2.keys()),'\n')

exec('global b   ;  b=2',d1,d2)
print(list(d1.keys()),'\n',list(d2.keys()),'\n')




















from os import system
system("echo 【按任意键以结束】 & pause>nul")
