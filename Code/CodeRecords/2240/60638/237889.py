import itertools
numbers=list(map(int ,input().split(",")))
ave=0
b=False
for i in range(0,len(numbers)):
    ave=ave+numbers[i]
    numbers[i]=numbers[i]*len(numbers)
for k in range(1,len(numbers)):
    for i in itertools.combinations(numbers,k):
        sum=0
        for j in i:
            sum=sum+j
        if sum==len(i)*ave:
            print(True)
            b=True
            break
    if b:
        break
if not b:
    print(False)
