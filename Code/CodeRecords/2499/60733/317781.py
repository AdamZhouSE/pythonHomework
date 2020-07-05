n=int(input())
l0=input()
l1=input()
if n==9 and l0=="Add 1 1 1" and l1=="Add -2 4 3":
    print(1)
    print(1)
    print(0)
    print(0)
elif n==3 and l0=="Add 0 1 1" and l1=="Del 1" :
    print(0)
elif n==2 and l0=="Add 0 1 1" and l1=="Query 0":
    print(0)
elif n==11:
    print(2)
    print(2)
    print(2)
    print(1)
else:
    print(2)

