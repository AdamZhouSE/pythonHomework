num=int(input())
for k in range(num):
    n=int(input())
    sum=0
    for i in range(n):
        sum=sum+3*i*i+3*i+2
    print(sum)