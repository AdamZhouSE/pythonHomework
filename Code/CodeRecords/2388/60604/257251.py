n=int(input())
for I in range(n):
    l=int(input())
    a1=input().split()
    a2=input().split()
    a1.sort()
    a2.sort()
    if a1==a2:
        print(1)
    else:print(0)