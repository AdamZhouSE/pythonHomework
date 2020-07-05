def check(number):
    i=number
    if i in [2,3,5,7]:
        return True
    for j in range(2,int(pow(i,0.5))+1):
        if i%j==0:
            return False
    return True

T=int(input())
for t in range(T):
    n=int(input())
    d=[]
    for i in range(2,n-1):
        if len(d)==3:
            break
        if n%i==0 and check(i):
            d.append(i)
    if len(d)<3:
        print(0)
    elif d[0]*d[1]*d[2]!=n:
        print(0)
    else:
        print(1)