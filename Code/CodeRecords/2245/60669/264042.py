n=bin(int(input()))
arr=[]
for i in range(0,len(n)):
    if n[i]=='1':
        arr.append(i)
if len(arr)==1:
    print(0)
else:
    temp=1
    for i in range(0,len(arr)-1):
        diff=arr[i+1]-arr[i]
        if diff > temp:
            temp=diff
    print(temp)
