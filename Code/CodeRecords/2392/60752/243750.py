num=int(input())
for i in range(num):
    line=list(map(int,input().split(' ')))
    size=line[0]
    x=line[1]
    eles=list(map(int,input().split(' ')))
    eles.sort()
    rs='No'
    for e in range(size-1):
        if eles[e]>=x:
            break
        for f in range(e+1,size):
            if eles[f]>=x:
                break
            if eles[e]*eles[f]==x:
                rs='Yes'
    print(rs)
            


