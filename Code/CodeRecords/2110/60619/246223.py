n = int(input())
while n % 3 == 0:
    n = int(n/3)
while n % 5 == 0:
    n = int(n/5)
while n % 2 == 0:
    n = int(n/2)
if n != 1:
    print(False)
else:
    print(True)