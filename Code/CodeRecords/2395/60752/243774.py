num=int(input())
for i in range(num):
    size=int(input())
    eles=list(map(int,input().split(' ')))
    zero=0
    if eles[0]==0:
        zero+=1
        eles.append(0)
    for e in range(1,size):
        if eles[e]==eles[e-1]:
            eles[e-1]=2*eles[e-1]
            eles[e]=0
            zero+=1
            eles.append(0)
        if eles[e]==0:
            zero+=1
            eles.append(0)
    for e in range(zero):
        eles.remove(0)
    print(' '.join(map(str,eles)))



