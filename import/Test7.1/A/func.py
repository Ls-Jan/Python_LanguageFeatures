import sys


[print(key) for key in [__name__,__file__,__package__]]
print()

def func(context):
    exec('from . import trigger')









