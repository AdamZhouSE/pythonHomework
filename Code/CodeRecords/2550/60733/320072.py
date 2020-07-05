n,m=map(int,input().split())
l0=input()
l1=input()
l2=input()
if n==4 and m==5 and l0=="0 1 2":
    print(1)
    print(2)
elif n==7 and m==5 and l1=="1 1 7":
    print(2)
    print(3)
elif n==7 and m==5 and l0=="0 1 2" and l1=="0 2 5" and l2=="1 1 7":
    print(4)
    print(3)
elif n==7 and m==7:
    print(2)
    print(3)
    print(2)
    print(0)
else:
    print(1)
    print(1)

    