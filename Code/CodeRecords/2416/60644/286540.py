t=input().split()
N=int(t[0])
M=int(t[1])
a=['0']*N
for i in range(0,M):
    num=int(input())
    a[num-1]=str(1-int(a[num-1]))
    b=''.join(a).split('1')
    for j in range(0,b.count('')):
        b.remove('')
    print(b.count('0')*2+1)
   
