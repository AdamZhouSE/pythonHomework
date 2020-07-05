def muteSequence(arr,n,m,c):
    res = []
    for i in range(0,len(arr)-m+1):
        if (max(arr[i:i + m]) - min(arr[i:i + m]))<=c:
            res.append(i+1)
    return res

temp = input().split()
n = int(temp[0])
m = int(temp[1])
c = int(temp[2])
temp = input().split()
arr = []
for t in temp:
    arr.append(int(t))
res = muteSequence(arr,n,m,c)
if(len(res)==0):
    print("NONE")
else:
    for i in res:
        print(i)