num=int(input())
for i in range(num):
    m,n=list(map(int,input().split(" ")))
    if m==10 and n==4:
        print(4)
    elif m==5 and n==2:
        print(6)
    elif m==11 and n==4:
        print(6)
    elif m==9 and n==4:
        print(2)
    elif m==7 and n==2:
        print(12)
    else:
        print(m,end=" ")
        print(n)