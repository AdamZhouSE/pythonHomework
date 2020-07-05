import re

sea=re.compile('\d+')
num=sea.findall(input())
k=int(input())
x=int(input())
result=[]
position=0
for i in range(len(num)):
    if int(num[i])>=x:
        position=i
        break
#此处得到判断的基准位置

start=position-1
end=position
for n in range(k):
    if  start==-1:
        for i in range(k-n):
            result.append(int(num[end+i]))
        break
    else:
        if end==len(num)+1:
            for i in range(k-n):
                result.append(int(num[start-i]))
            break
        else:#这里开始比较大小
            if x-int(num[start])<=int(num[end])-x:
                result.append(int(num[start]))
                start-=1
            else:
                result.append(int(num[end]))
                end+=1
result.sort()
print(result)