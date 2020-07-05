n=int(input())
for x in range(0,n):
    num=int(input())
    numbers=list(map(int,input().split(" ")))
    length=0
    for i in range(0,num-1):
        for j in range(i+1,num):
            if numbers[j]>numbers[i]:
                length=max(length,j-i)
    print(length)
 