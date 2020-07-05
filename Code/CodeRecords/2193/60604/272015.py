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
        if a[len(a)-1-i]==b[len(b)-1-i]:
            res+=1
        else:
            return res
    return res

for I in range(m):
    tmp=[]
    res=[]
    x=input().split()
    for i in range(2):
        x[i]=int(x[i])
    #print(x)
    #print(s)
    for i in range(x[0],x[1]+1):
        tmp.append(s[0:i])
   # print(tmp)
    for i in range(len(tmp)-1):
        for j in range(i+1,len(tmp)):
            res.append(mmm(tmp[i],tmp[j]))
    res.sort()
    print(res[-1])
tmp.sort()
#print(tmp[-1])



















