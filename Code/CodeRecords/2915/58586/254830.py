n=int(input())
arr=list(map(int,input().split(" ")))
arr.sort()
pre=arr[0]
count=1
longest=1
for i in range(1,n):
    if arr[i]>pre and arr[i]<=2*pre:
        count+=1
        longest=max(longest,count)
    else:
        count=1
    pre=arr[i]
print(longest)