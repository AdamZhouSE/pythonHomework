n = int(input())
while(n>0):
    el=int(input())
    if(el%2==0):
        e=int(el/2)-1
        re=pow(2,pow(3,e))
    else:
        e=int(el/2)
        re=pow(2,pow(2,e))
    print(re)
    n=n-1