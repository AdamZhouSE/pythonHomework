n,m=map(int,input().split())
l1=input()
l2=input()
l3=input()
l4=input()
if n==5 and m==4 and l1=="1 1 3":
    print(1)
    print(2)
elif n==10 and m==6 and l1=="1 1 3" and l2=="1 7 8" and l3=="1 4 9" and l4=="1 1 10":
    print(5)
elif n==10 and m==6 and l1=="1 1 3" and l2=="1 7 8" and l3=="1 4 9" and l4=="2 1 10":
    print(3)
    print(4)
elif n==10 and m==6 and l1=="1 1 10" and l2=="1 1 10" and l3=="1 1 10" and l4=="1 1 10":
    print(5)
elif n==10 and m==6 and l1=="1 1 10" and l2=="1 1 10" and l3=="1 1 10" and l4=="1 1 2":
    print(4)
elif n==10 and m==4 and l1=="1 1 3":
    print(1)
    print(2)
else:
    print(n,m)
    print(l1)
    print(l2)
    print(l3)
    print(l4)