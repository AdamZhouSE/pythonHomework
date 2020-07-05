import re
str = input()
list = re.split('\[|,|\]',str)
list.remove("")
list.remove("")
list=sorted(list)
print('[',end="")
for i in range(0,len(list)):
    if i == 0:
        print(list[i],end="")
    else:
        print(", "+list[i],end="")
print(']')