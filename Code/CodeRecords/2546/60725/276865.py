p=[]
p[0]='1'
p[1]='1'
p[2]='1'
for j in range(3,100):
    p[j]=p[j-2]+p[j-3]
T=int(input())
for i in range(T):
    d=int(input())
    print(p.index(d))

