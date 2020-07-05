n=int(input())
lsa=[]
lsb=[]
for i in range(n):
    t1,t2=map(int,input().split(' '))
    lsa.append(t1)
    lsb.append(t2)
t=0
for i in range(n):
    for j in range(n):
        if lsa[i]<lsa[j] and lsb[i]>lsb[j]:
            print('Happy Alex')
            t=1
            break
    if t==1:
        break
    if i==n-1:
        print('Poor Alex')
        break