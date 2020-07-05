numof=int(input())
i=0
n=1
n1=1
while(i<numof):
    n=n1
    check=True
    if(n==2 or n==3 or n==5):
        check=True
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
    if(check):
        i=i+1
    n1=n1+1
print(n1-1)