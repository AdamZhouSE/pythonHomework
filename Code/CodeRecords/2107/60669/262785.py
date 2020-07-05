n=int(input())
if n<=0:
    print(False)
else:
    while True:
        if n==1:
            print(True)
            break
        if n%2==0:
            n/=2
        else:
            print(False)
            break