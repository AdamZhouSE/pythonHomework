n=int(input())
l=[]
r=[]
for i in range(0,n):
    l.append(int(input()))
def test_prime(n):
    if (n==1):
        return False
    elif (n==2):
        return True;
    else:
        for x in range(2,n):
            if(n % x==0):
                return False
        return True
for i in range(0,n):
    x=l[i]+2
    if(test_prime(x)==True):
        r.append("Yes")
    else:
        r.append("No")
for i in range(0,n):
    print(r[i])
