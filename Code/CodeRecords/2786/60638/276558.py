n=int(input())
numbers=list(map(int,input().split(" ")))
count=0
for i in range(1,n+1):
    minN=10000000
    k=-1
    for j in range(0,len(numbers)):
        if numbers[j]>=i:
            if minN>numbers[j]:
                minN=numbers[j]
                k=j
    if k==-1:
        print(count)
        break
    else:
        numbers.remove(minN)
        count=count+1
        if i==n:
            print(count)