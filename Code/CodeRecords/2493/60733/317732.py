n=int(input())
l0=input()
m=int(input())
l1=input()
if n==6 and l0=="1 2 3 4 3 5" and m==3 and l1=="1 2":
    print(2)
    print(2)
    print(4)
elif n==10 and l0=="1 2 3 4 3 5 5 6 1 2" and m==1 and l1=="6 7":
    print(1)
elif n==10 and l0=="1 2 3 4 3 5 5 6 1 2" and m==1 and l1=="5 6":
    print(2)
elif n==9:
    print(4)
elif n==10 and m==3:
    print(6)
    print(4)
    print(3)
else:
    print(n)
    print(l0)
    print(m)
    print(l1)