num=int(input())
for k in range(num):
    n=int(input())
    sum=0
    for i in range(n):
        for j in range(i+1):
            sum=sum+j+1
    print(sum)
