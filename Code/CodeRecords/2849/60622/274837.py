arr_len=int(input())
arr=list(map(int,input().split()))
arr.sort()
ans=True
for i in range(arr_len):
    if arr[i]%arr[0]!=0:
        ans=False
        break
if ans==True:
    print(arr[0])
else:
    print(-1)