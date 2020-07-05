numbers=list(map(int,input().split(",")))
maxN=0
for i in range(0, len(numbers)):
    sum=0
    for j in range(0, len(numbers)):
        sum=sum+j*numbers[(len(numbers)-i+j)%len(numbers)]
    maxN=max(sum,maxN)
print(maxN)