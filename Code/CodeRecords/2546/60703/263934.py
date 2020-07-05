T = int(input())

def padovan(n):
    if(n==0 or n==1 or n==2):
        return 1
    else:
        return padovan(n-2)+padovan(n-3)
for i in range(T):
    n = int(input())
    print(padovan(n))