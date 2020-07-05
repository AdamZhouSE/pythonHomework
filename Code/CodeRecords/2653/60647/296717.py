n=int(input())
for i in range(n):
    list=input().split()
    a=int(list[0])
    b=int(list[1])
    if b<=10:
        res=(a-1)*10-(a-1)*b
        print(res)
    else:
        print(0)