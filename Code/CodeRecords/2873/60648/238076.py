n,m=map(int,input().split())
ls=input().split(" ")
ls=[int(ls[i]) for i in range(n)]
ls1=input().split(" ")
ls1=[int(ls1[k]) for k in range(m)]
#s=""
lsr=[]
for i in ls:
    for j in ls1:
        if i==j:
            #s=s+str(i)+" "
            lsr.append(str(i))
            break
#s.rstrip()
#print(s,end='')
s1=" ".join(lsr)
print(s1)