x=input().split()
n=int(x[0])
m=int(x[1])
s=input()
def mmm(a,b):
    l=len(a)
    if len(a)>len(b):
        l=len(b)
    res=0
    for i in range(l):
        if a[i]==b[i]:
            res+=1
        else:
            return res
    return res
tmp=[]
for I in range(m):
    x=input().split()
    for i in range(4):
        x[i]=int(x[i])
    tmp1=s[x[0]-1:x[1]]
    tmp2=s[x[2]-1:x[3]]
    print(mmm(tmp1,tmp2))
    tmp.append(mmm(tmp1,tmp2))
tmp.sort()
#print(tmp[-1])