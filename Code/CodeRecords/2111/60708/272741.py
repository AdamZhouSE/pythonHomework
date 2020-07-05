n=int(input())
result=0
for i in range(0,n):
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
    if(check):
        result=result+1
print(result)