num=int(input())
for i in range(num):
    size=int(input())
    eles=list(map(int,input().split(' ')))
    count=0
    for j in range(size-1):
        ele1=eles[j]
        for k in range(j+1,size):
            ele2=eles[k]
            if ele1>ele2:
                count+=1
    print(count)