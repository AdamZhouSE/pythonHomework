n=int(input())
def Padovan(n):
    if(n==0 or n==1 or n==2):
        return 1
    else:
        return Padovan(n-2)+Padovan(n-3)
for i in range(n):
    N=int(input())
    print(Padovan(N))