arr=list(map(int,input().split(",")))
target=int(input())
res=0
if min(arr)*len(arr)<=target:
    res=min(arr)
begin=res
values=[]
while res<max(arr):
    arr.append(res)
    arr.sort()
    i=arr.index(res)
    sum1=sum(arr[0:i])+(len(arr)-i-1)*res
    values.append(abs(sum1-target))
    res+=1
print(begin+values.index(min(values)))