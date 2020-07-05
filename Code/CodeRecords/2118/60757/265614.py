n=int(input())
while(True):
    if n==0:
        print(False)
        break
    if n==1:
        print(True)
        break
    if n%3==0:
        n=n/3
    else:
        print(False)
        break