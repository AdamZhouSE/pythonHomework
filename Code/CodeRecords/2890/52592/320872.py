S=input().split(' ')
n=int(S[0])
x=int(S[1])
y=int(S[2])
enemy=[]
N=n
ks=[]
for i in range(n):
    enemy.append(input().split(' '))
for i in enemy:
    if(int(i[0])-x==0):
        k=999
    else:
        k=(int(i[1])-y)/(int(i[0])-x)
    if k not in ks:
        ks.append(k)
print(len(ks))
    
    