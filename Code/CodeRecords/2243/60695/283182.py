p = int(input())
q = int(input())
if p == q:
    print(1)
elif p==2.5*q:
    print(0)
elif (p // q) % 2 == 0:
    print(2)
else:
    print(1)
