def padovan(n):
    if((n==0)|(n==1)|(n==2)):
        return 1
    else:
        return padovan(n-2)+padovan(n-3)
t=int(input())
for i in range(t):
    print(padovan(int(input())))