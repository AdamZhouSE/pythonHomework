num=int(input())
for k in range(num):
    n=int(input())
    sum=0
    for i in range(n):
        sum=(i+1)*(i+1)+sum
    print(sum)