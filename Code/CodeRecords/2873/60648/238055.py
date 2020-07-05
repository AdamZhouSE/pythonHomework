n,m=map(int,input().split())
ls=input().split(" ")
ls=[int(ls[i]) for i in range(n)]
ls1=input().split(" ")
ls1=[int(ls1[i]) for i in range(m)]
s=""
for i in ls:
    for j in ls1:
        if i==j:
            s=s+str(i)+" "
            break
print(s.rstrip)