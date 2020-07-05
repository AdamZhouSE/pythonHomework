n=int(input())
if n==1:
    print(True)
    exit()
if n%2!=0 or n<=0:
    print(False)
    exit()
while n>1:
    if n%2!=0:
        print(False)
        exit()
    n/=2
print(True)