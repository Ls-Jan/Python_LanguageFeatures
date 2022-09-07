

print("TRIGGER!!!!!!!!!!!!!!!!!!!!")
[print('{:20}'.format(key),eval(key)) for key in dir() if key.find('builtins')==-1]#不输出builtins是因为太烦，又臭又长
print()
