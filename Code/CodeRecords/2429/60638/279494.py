n=int(input())
for x in range(0,n):
    num=int(input())
    numbers=list(map(int,input().split(" ")))
    maxN=0
    for i in range(0,num-1):
        for j in range(i+1,num):
            if numbers[j]>=numbers[i]:
                maxN=max(maxN,numbers[j]-numbers[i])
    print(maxN)