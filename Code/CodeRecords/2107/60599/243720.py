n=int(input())
k=1
while(1):
    if k==n:
        print(True)
        exit()
    if k>n:
        print(False)
        exit()
    k*=2
