N=input()
x=2*N
res=1
index=int((N+1)/2)
for n1 in range(1,index):
    for n2 in range(2,index+1):
        if (n1+n2)*(n2-n1+1)==x:
            res+=1
print(res)