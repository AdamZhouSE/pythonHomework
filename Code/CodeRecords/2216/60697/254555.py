s=input()
dol=[]
den=[]
sign=[]
if(s[0]=='-'):
    s="0/1"+s
size=len(s)
i=0
dol.append(int(s[i]))
i=i+2
den.append(int(s[i]))
i=i+1
while i<size:
    sign.append(s[i])
    i+=1
    dol.append(int(s[i]))
    i+=2
    den.append(int(s[i]))
    i+=1
tmp={}
for j in den:
    if j not in tmp:
        tmp[j]=1
maxden=1
for j in tmp.keys():
    maxden*=j
for i in range(len(dol)):
    dol[i]=dol[i]*maxden//den[i]
res=dol[0]

for i in range(len(dol)-1):
    if(sign[i]=="+"):
        res+=dol[i+1]
    else:
        res-=dol[i+1]

if(res==0):
    print("0/1")
else:
    res=int(res)
    maxden=int(maxden)
    k=min(res,maxden)
    while k>0:
        if(res%k==0 and maxden%k==0):
            res=res//k
            maxden=maxden//k
            break
        k-=1
    s=str(res)+"/"+str(maxden)
    print(s)







