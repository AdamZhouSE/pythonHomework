def ma(m1,m2):
    r=[]
    for i in range(len(m1)):
        t=[]
        for j in range(len(m1)):
            t.append(0)
        r.append(t)
    for i in range(26):
        for j in range(26):
            this=0
            for k in range(26):
                n1=m1[i][k]
                n2=m2[k][j]
                this=this+n1*n2
            r[i][j]=this
    return r
N = int(input())
s = input()
ls = []
m=[]
for i in range(26):
    this=[]
    for j in range(26):
        a = chr(i + ord('a'))
        b = chr(j + ord('a'))
        if s.__contains__(a + b):
            this.append(0)
        else:
            this.append(1)
    ls.append(this)
    n=2
for i in range(26):
    this=[]
    for j in range(26):
        this.append(ls[i][j])
    m.append(this)

b=bin(N-2)[2:]#需要乘N-2次
lss=[]
i=0
while i<len(b) and N>2:
    if b[len(b)-1-i]=='1':
        lss.append(m)
    if i==len(b)-1:
        break
    mm=[]
    for j in range(len(m)):
        this=[]
        for k in range(len(m)):
            this.append(m[j][k])
        mm.append(this)
    m=ma(m,mm)
    i=i+1
#print(m)
#print(lss)
i=0
while i<len(lss):
    ls=ma(ls,lss[i])
    i=i+1

result=0
for i in range(26):
    for j in range(26):
        result=result+ls[i][j]
if N==1:
    result=26
print(result)






