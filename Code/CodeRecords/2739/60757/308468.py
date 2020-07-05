import math
li=input().split(', ')
k=int(li[0])
n=int(li[1])
maxk=int(math.pow(10,k))
beg=int(math.pow(10,k-1))
re=[]
for i in range(beg,maxk):
    s=list(map(int,tuple(set(list(str(i))))))
    if len(s)==k:
        sign=1
        su=0
        for j in range(k):
            su=su+int(s[j])
            if s[j]==0:
                sign=0
        if sign==1:
            if su==n:
                if re.count(sorted(s))==0:
                    re.append(sorted(s))            
print(re)
               
        