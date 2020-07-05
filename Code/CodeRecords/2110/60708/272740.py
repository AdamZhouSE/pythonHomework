n=int(input())
check=True
if(n==2 or n==3 or n==5):
    check=False
else:
    while (check):
        if (n % 2 == 0):
            n = int(n / 2)
        elif (n % 3 == 0):
            n = int(n / 3)
        elif (n % 5 == 0):
            n = int(n / 5)
        elif (n == 1):
            break
        else:
            check = False
            break

print(check)