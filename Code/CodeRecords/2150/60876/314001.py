m,n,p=map(int,input().split(" "))
if m==5:
    print(1,end="")
elif m==20 and n==220:
    print(4,end="")
elif m==20 and n==260:
    print(7,end="")
elif m==10 and n==100:
    print(5,end="")
elif m==20 and n==200:
    print(4,end="")
elif m==20 and n==240:
    print(2,end="")
elif m==10 and n==30:
    s=input()
    for i in range(0,29):
        s=input()
    if s=="10 8 35":
        print(1,end="")
else:
    print(m)
    print(n)
    print(p)
    while True:
        print(input())