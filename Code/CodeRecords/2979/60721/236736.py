import re
str=input()
list=re.findall(r"[a-z]{1,}",str)
x=0
for i in range(1,len(list)):
    if(len(list[i])>len(list[x])):
        x=i
print(list[x])
