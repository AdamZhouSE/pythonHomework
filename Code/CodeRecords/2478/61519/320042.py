n=int(input())
for i in range(n):
    num=list(input().split(" "))
    a=int(num[0])
    b=int(num[1])
    m=int(input())
    d=b-a
    print(a+(m-1)*d)