candies=int(input())
n=int(input())
ans=[0 for i in range(0,n)]
count=0
ptr=0
while candies>0:
    count+=1
    if candies-count>=0:
        candies-=count
        ans[ptr%n]+=count
    else:
        candies=0
        ans[ptr%n]+=candies
    ptr+=1
print(ans)