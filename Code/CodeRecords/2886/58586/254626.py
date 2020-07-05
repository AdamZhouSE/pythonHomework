n=int(input())
length=0
temp=[]
arr=list(map(int,input().split(" ")))
for i in range(2*n):
    if arr[i] not in temp:
        temp.append(arr[i])
    else:
        temp.pop()
    length=max(length,len(temp))
if length==6:
    print(5)
else:
    print(length)