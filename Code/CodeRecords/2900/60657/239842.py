import re
a=input()
a=re.findall(r'[^ \n]',a)
print(len(a))
