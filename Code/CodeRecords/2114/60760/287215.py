sum=int(input())
res=[i for i in range(sum+1)]
for i in range(2,sum+1):
    for j in range(1,int(i**0.5)+1):
        res[i]=min(res[i],res[i-j*j]+1)

print(res[-1])
