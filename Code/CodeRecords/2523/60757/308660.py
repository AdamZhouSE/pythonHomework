arr=eval(input())
m=len(arr)
n=len(arr[0])
t=min(m,n)
for i in range(n):
    y=i
    x=0
    tmp=[]
    for j in range(t):
        if x<m:
            if y<n:
                tmp.append(arr[x][y])
                x+=1
                y+=1
    tmp=sorted(tmp)
    y=i
    x=0
    for j in range(t):
        if x<m:
            if y<n:
                arr[x][y]=tmp[j]
                x+=1
                y+=1
for i in range(1,m):
    y=0
    x=i
    tmp=[]
    for j in range(t):
        if x<m:
            if y<n:
                tmp.append(arr[x][y])
                x+=1
                y+=1
    tmp=sorted(tmp)
    y=0
    x=i
    for j in range(t):
        if x<m:
            if y<n:
                arr[x][y]=tmp[j]
                x+=1
                y+=1
print(arr)                