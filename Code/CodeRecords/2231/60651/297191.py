a=[]
b=[]
for i in range(2,100):
    flag=0
    for j in range(2,i):
        
        if i%j==0:
            flag=1
    if flag==0:
        a.append(i)
for i in a:
    for j in a:
        for k in a:
            if i!=j and i!=k and j!=k:
                b.append(i*j*k)
t=int(input())
for i in range(t):
    num=int(input())
    if num in b:
        print(1)
    else:
        print(0)