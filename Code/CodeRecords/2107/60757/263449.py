n=int(input())
while(True):
    if n==1:
        print(True)
        break
    if n%2==0:
        n=n/2
    else:
        print(False)
        break