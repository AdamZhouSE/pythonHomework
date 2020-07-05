n,m,c=map(int,input().split(" "))
nums=list(map(int,input().split(" ")))
result=[]
sum=1
for i in range(1,n):
    if nums[i]-nums[i-1]>=-c and nums[i]-nums[i-1]<=c:
        sum+=1
    else:
        sum=1
    if sum>=m:
        result.append(i-m+2)
if result==[]:
    print("NONE",end="")
else:
    for item in result:
        print(item)