num=int(input())
for i in range(num):
    n=int(input())
    li=input().split(' ')
    k=int(input())
    li=list(map(int,li))
    sum=1
    for i in range(n):
        sum=sum*li[i]
    print(sum%k)