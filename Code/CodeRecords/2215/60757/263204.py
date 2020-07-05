arr=eval(input())
if len(arr)==1:
    print(arr[0])
if len(arr)==2:
    print(str(arr[0])+'/'+str(arr[1]))
n=len(arr)
result=float(arr[0])
for i in range(1,n):
    result=result/float(arr[i])
tmp=1/float(arr[1])*float(arr[0])
for i in range(2,n):
    tmp=tmp*float(arr[i])
if(tmp>result):
    print(str(arr[0])+'/(',end='')
    for i in range(1,n-1):
        print(str(arr[i])+'/',end='')
    print(str(arr[n-1])+')')
else:
    for i in range(n-1):
        print(str(arr[i])+'/',end='')
    print(str(arr[n-1]))