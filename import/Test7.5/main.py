
print("【Test 7.5】")
print()


context={'__name__':'A.XXXXXXXXXXXXX'}
exec('from . import trigger',context)
print(f'【{context.keys()}】')





# [print(key) for key in [__name__,__file__,__package__]]
# print()

# from A.func import func
# func(globals())




















