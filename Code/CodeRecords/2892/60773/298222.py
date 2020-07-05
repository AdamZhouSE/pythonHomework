l=input().split(" ")
#print(l)
n1=int(l[0])
n2=int(l[1])
s=""
res=[]
for i in range(10):
    res.append(0)
for i in range(n1,n2+1,1):
    if n1+i!=0:
        s=s+str(i)
for j in range(len(s)):
    res[int(s[j])]=res[int(s[j])]+1
for i in range(10):
    if i!=9:
        print(res[i],end=" ")
    else:
        print(res[i],end="")
#print("")
