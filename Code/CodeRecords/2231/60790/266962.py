def resolve(n):
    m=[]
    for i in range(2,n+1):
        while(n%i==0 and n!=1):
            m.append(i)
            n=n/i
    return m
t=int(input())
for j in range(0,t):
    mi=resolve(int(input()))
    set1=set(mi)
    if(len(mi)==3 and len(set1)==3):
        print(1)
    else:
        print(0)
        