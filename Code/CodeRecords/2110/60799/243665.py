n = int(input())
if n<= 0:
    print(False)
else:
    while n % 2 == 0:
        n = int(n/2)
    while n % 3 == 0:
        n = int(n/3)
    while n % 5 == 0:
        n = int(n/5)
    print(n==1)