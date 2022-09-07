import sys


[print(key) for key in [__name__,__file__,__package__]]
print()

def func(context):
    ctx={'__name__':''}
    exec('from . import trigger',ctx)
    print(f'【{ctx}】')








