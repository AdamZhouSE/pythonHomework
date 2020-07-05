case=int(input())

for m in range(case):
    train=int(input())
    arrive=[int(x) for x in input().split(' ')]
    leave=[int(x) for x in input().split(' ')]
    plat=1
    i=1
    while(i<len(arrive)):
        add=True
        j=0
        while(j<i):
            if(arrive[i]>leave[j]):
                del arrive[j]
                del leave[j]
                i-=1
                add=False
                break
            j+=1
        if(add):
            plat+=1
        i+=1
        
    print(plat)
            