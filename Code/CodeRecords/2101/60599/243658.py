def happy(a):
    res=0
    while a!=0:
        res+=(a%10)**2
        a//=10
    return res
n=int(input())
k=0
while k<100:
    n=happy(n)
    if(n==1):
        print('True')
        exit()
    k+=1
print('False')