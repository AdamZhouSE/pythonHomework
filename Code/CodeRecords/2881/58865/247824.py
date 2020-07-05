n=int(input())
arr=[]
#防止每一行引用同一组0的地址
for i in range(n):
    arr.append(['D']*n)
for i in range(n//2):
    for j in range(n):
        if abs(j-(n-1)/2)>=i%((n-1)/2)+1:
            arr[i][j]='*'
for i in range(n//2,n):
    arr[i]=arr[n-i-1]
for i in arr:
    print(''.join(i))