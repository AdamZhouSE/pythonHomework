n=int(input())
def func(l):
    f=int(l/5)
    if(f==1):
        return 1
    return int(f/2)+1

for i in range(n):
    m=int(input())
    k=int(m/3)
    re=[]
    for j in range(k+1):
        if((m-3*j)%5==0):
            z=func(m-3*j)
            re.append(z)
    print(sum(re))