def ma(m1,m2):
    for i in range(26):
        for j in range(26):
            this=0
            for k in range(26):
                this=this+m1[i][k]*m2[k][j]
            m1[i][j]=this
    return m1
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
    m.append(this)
    n=2
while n<N:
    ls=ma(ls,m)
    n=n+1

result=0
for i in range(26):
    result=result+ls[i].count(1)

print(result)






