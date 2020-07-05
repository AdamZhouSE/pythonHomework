n=int(input())

for i in range(0,n):
    a=int(input())
    if int(int(a**0.5)**2) == a:
        print(1)
    else:
        print(0)