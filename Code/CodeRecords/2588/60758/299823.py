prime=[2]
for i in range(int(1e3)):
    for j in range(2,i):
        if i%j==0:
            break
        if j ==i-1:
            prime.append(i)

for _ in range(int(input())):
    n=input()
    total=0
    for i in n:
        total+=int(i)
    n=int(n)
    y=n
    get=[]
    index=0
    while n!=1:
        x=prime[index]
        if n%x==0:
            n/=x
            s=str(x)
            for k in s:
                get.append(int(k))
        else:
            index+=1
    if (total==sum(get) and y not in prime) or y==1:
        print(1)
    else:
        print(0)