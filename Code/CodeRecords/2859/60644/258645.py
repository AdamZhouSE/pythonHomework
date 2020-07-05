line=int(input())
arr=[]
for i in range(0,line):
    arr=arr+[input()]
for i in range(0,line):
    arr[i]=list(arr[i])
x=''
res=True
for i in range(0,line):
    if arr[i][i]!=arr[i][-i-1]:
        res=False
        break
for i in range(0,line-1):
    if arr[i][i]!=arr[i+1][i+1]:
        res=False
        break

if res:
    x=arr[0][0]
    for i in range(0,line):
        for j in range(0,2):
            try:
                arr[i].remove(x)
                

            except:
                continue

    for i in range(0,line):
        if i!=(line-1)/2:
            if arr[i].count(arr[i][0])!=line-2 or arr[i][0]==x:
                res=False
                break
        else:
            if arr[i].count(arr[i][0])!=line-1 or arr[i][0]==x:
                res=False
                break
if res:
    print('YES')
else:
    print('NO')
