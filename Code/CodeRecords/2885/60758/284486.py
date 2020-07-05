n=int(input())
for i in range(n):
    x=int(input())
    num=list(map(int,input().split()))
    a=sum(num)
    print(int(a/3))