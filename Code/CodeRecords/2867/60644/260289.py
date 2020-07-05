arr=[]
for i in range(0,5):
    arr=arr+[input().split()]
x=y=0
for i in range(0,5):
    for j in range(0,5):
        if arr[i][j]=='1':
            x=i
            y=j
            break
print(abs(x-2)+abs(y-2))

