arr=list(map(int,input().split(",")))
num=-1
result=[]
for i in range(1,len(arr)):
    if arr.count(i)==2:
        num=i
        result.append(i)
        break
for i in range(1,len(arr)):
    if arr.count(i)==0:
        result.append(i)
        break
print(result)