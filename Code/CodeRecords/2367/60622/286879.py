arr=[1,11,111,1111,11111,111111,1111111,11111111,111111111,1111111111,11111111111]
n=int(input())
ans=[]
for i in range(len(arr)):
    if arr[i]%n==0:
        ans.append(len(str(arr[i])))
ans.sort()
if len(ans)==0:
    ans.append(-1)
print(ans[0])