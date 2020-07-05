n=eval(input())
arr=list(map(int,input().strip().split(' ')))
arr=sorted(arr)
ifWin=False
for i in range(n-2):
    if arr[i]+arr[i+1]>arr[i+2]:
        ifWin=True
        break
if ifWin:
    print('YES')
else:
    print('NO')
        