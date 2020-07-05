import re
a=input()
cons1=[]
for i in range(0, 20000):
    cons1.append(str(i))
str1=''.join(cons1)
re.findall(r'[\d]',str1)
print(str1[int(a)])