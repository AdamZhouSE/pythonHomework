arr=eval(input())
le=len(arr)
num=0
result=[]
while num<le-1:
    curmax=max(arr)
    index=arr.index(curmax)
    if index!=le-num-1:
        result.append(index+1)
        result.append(le-num)
        temp=arr[:index+1][::-1]+arr[index+1:]
        arr=temp[::-1][:-1]
    else:
        arr=arr[:-1]
    num=num+1
if result==[1,2]:
    result=[2]

print(result)