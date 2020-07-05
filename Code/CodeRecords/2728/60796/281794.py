N=int(input())
r=[]
while N>0:
    n=int(input())
    ls=input().split(" ")
    for i in range(n):
        ls[i]=int(ls[i])

    max=0
    for i in range(n-1):
        for j in range(n):
            t=(j-i)*min(ls[i],ls[j])
            if t>max:
                max=t
    r.append(max)
    N=N-1
for j in range(len(r)):
    print(r[j])