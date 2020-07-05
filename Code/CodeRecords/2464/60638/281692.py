maxN=int(input())
numbers=list(map(int,input().split(",")))
minLen=10000
for i in range(0,len(numbers)):
    length=0
    sum=0
    for j in range(i,len(numbers)):
        if sum>=maxN:
            break
        sum=sum+numbers[i]
        length+=1
    if sum>=maxN:
        minLen=min(minLen,length)
print(minLen)