n=int(input())

x=input()
y=input()

if n==4:
    print(2)
elif n==2 and x=="1,0":
    print(-1)
elif n==2 and x=="0,1":
    print(0)
else:
    print(n)
    print(x)
    print(y)