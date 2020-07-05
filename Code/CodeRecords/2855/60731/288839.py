n=int(input())
data=[]
judge=True
for i in range(n):
    str=input()
    data.append(str)
for j in range(n):
    for k in range(n):
        numofo=0
        up=j-1
        down=j+1
        left=k-1
        right=k+1
        if up>=0:
            if data[up][k]=='o':
                numofo+=1
        if down<=n-1:
            if data[down][k]=='o':
                numofo+=1
        if left>=0:
            if data[j][left]=='o':
                numofo+=1
        if right<=n-1:
            if data[j][right]=='o':
                numofo+=1
        if numofo%2!=0:
            judge=False
            break
if judge:
    print('YES')
else:
    print('NO')