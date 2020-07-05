s=list(input())
s1=s.copy()
b=list(input())
bad=[]
for bb in range(len(b)):
    if b[bb]=='0':s1[bb]="-"+s1[bb]
k=int(input())
rs=[]
l=len(s)
good=[]

while l>0:
    for ll in range(len(s)-l+1):
        ss=' '.join(s1[ll:ll+l])
        sss=' '.join(s[ll:ll+l])
        if ss.count("-")<=k:
            if good.count(sss)==0:good.append(sss)
    l-=1

print(len(good))