import re
list=[int(x) for x in re.sub(r'[\[\],]',' ',input()).split()]
num=1
for i in range(len(list)):
    if i+1<len(list)and list[i]<list[i+1]:
        num+=1
print(num)


