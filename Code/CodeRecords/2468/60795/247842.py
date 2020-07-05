T=int(input())
for i in range(0,T):
    n=int(input())
    num=[int(n) for n in input().split(' ')]
    re=[]
    for j in range(0,n):
        pos=1
        for k in range(0,n):
           if k==j:
               continue
           else:
               pos=pos*num[k]
        re.append(pos)
    str=""
    for z in range(0,n):
        print(re[z],end=' ')
    print('')