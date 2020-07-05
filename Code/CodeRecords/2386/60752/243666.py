num=int(input())
for i in range(num):
    size=int(input())
    eles=list(map(int,input().split(' ')))
    sum=int(input())
    found=0
    for a in range(size-3):
        ele1=eles[a]
        for b in range(a+1,size-2):
            ele2=eles[b]
            for c in range(b+1,size-1):
                ele3=eles[c]
                for d in range(c+1,size):
                    ele4=eles[d]
                    if ele1+ele2+ele3+ele4==sum:
                        found=1
                        break
    print(found)


