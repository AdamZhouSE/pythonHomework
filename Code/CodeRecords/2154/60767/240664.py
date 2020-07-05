import copy
num = list(input())
temp = copy.copy(num)
temp.reverse()
flag = 1
for i in range(0,len(num)):
    if(num[i]!=temp[i]):
        flag = 0
        break
if(flag==0):
    print(False)
else:
    print(True)