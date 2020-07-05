numbers=list(map(int,input().split(",")))
k=int(input())
find=False
for i in range(0,len(numbers)):
    for j  in range(i+1,len(numbers)):
        sum=0
        for x in range(i,j+1):
            sum=sum+numbers[x]
        if sum%k==0:
            find=True
            break
        if find:
            break
    if find:
        break
print(find)