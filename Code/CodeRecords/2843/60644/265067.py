num=int(input())
arr=input().split()
for i in range(0,num):
    arr[i]=int(arr[i])
res=[0]*num
ans=''
res[num-1]=arr[num-1]
for i in range(num-2,-1,-1):
    res[i]=arr[i]+arr[i+1]
for i in range(0,num):
    ans=ans+' '+str(res[i])
print(ans[1:])
