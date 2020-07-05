
a=input()
a=a[1:len(a)-1]
store=[]
store.append(list(map(int, a.split(","))))
arr=store[0]
k=int(input())
x=int(input())
len=len(arr)
left=0
right=len-1
while len>k:
    if abs(arr[left]-x)>abs(arr[right]-x):
        left+=1
    else:
        right-=1
    len-=1
result=[]
for x in range(left,right+1):
    result.append(arr[x])
print(result)

