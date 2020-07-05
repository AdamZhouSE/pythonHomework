n=int(input())
if n<1:
    print(False)
    exit()
while n>1:
    if n%3!=0:
        print(False)
        exit()
    n/=3
print(True)