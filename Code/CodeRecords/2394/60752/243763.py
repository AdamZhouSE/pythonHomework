num=int(input())
for i in range(num):
    size=int(input())
    eles=list(map(int,input().split(' ')))
    zero=0
    for e in range(size):
        if eles[e]==0:
            zero+=1
            eles.append(0)
    for e in range(zero):
        eles.remove(0)
    print(' '.join(map(str,eles))+' ')
            


