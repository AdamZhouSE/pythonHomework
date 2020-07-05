test=int(input())
for i in range(test):
    size=int(input())
    eles=list(map(int,input().split(' ')))
    eles.sort()
    tri=0
    for a in range(0,size-2):
        ele1=eles[a]
        for b in range(a+1,size-1):
            ele2=eles[b]
            for c in range(b+1,size):
                ele3=eles[c]
                if ele1+ele2>ele3 and ele3-ele1<ele2:
                    tri+=1
    print(tri)
