def bits(j):
    p=j
    t=0
    while p>0:
        p=int(p/10)
        t+=1
    return t

a=[1]
k,m=input().split()
k=int(k)
m=int(m)
i=3
num=1
cont=[[] for i in range(10)]
cont[1].append(0)
while k>1:
    p=(i-1)/2
    q=(i-5)/4
    if (p in a) or (q in a):
        j=i
        w=bits(j)
        for p in range(w):
            n=j%10
            cont[int(n)].append(num+w-p-1)
            j=int(j/10)
        a.append(i)
        num+=w
        k-=1
    i+=2
# for i in range(len(a)-1): print(a[i],end='')
# print(a[-1])
s=""
for j in range(len(a)): s+=str(a[j])
print(int(s))
last=9
ans=""
loc=0
while(m>0 and last>0):
    size=len(cont[last])
    if(size==0): 
        last-=1
        continue
    j=0
    if(loc>cont[last][-1]): 
        last-=1
        continue
    #print("last",last)
    while cont[last][j]<loc: j+=1
    left=j
    if(cont[last][j]==loc): left+=1
    #print(left)
    while(j<size and cont[last][j]<=m+j-left+loc): 
        #print(cont[last][j])
        j+=1
    j-=1
    #j-=left
    #print("j",j)
    if(j<left and cont[last][left-1]!=loc):
        last-=1
        continue
    m=m-cont[last][j]+j-left+loc
    loc=cont[last][j]+1
    ml=last
    #print("loc",loc)
    #print("m",m)
    for k in range(j+1-left): ans+=str(last)
    last-=1
for j in range(loc,len(s)):
    if(m>0 and s[j]==str(ml)): 
        m-=1
        continue
    ans+=s[j]
print(int(ans),end='')