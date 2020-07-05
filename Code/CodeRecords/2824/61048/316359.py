def arr36():
    line1=input().split(' ')
    n,t,c=int(line1[0]),int(line1[1]),int(line1[2])
    crimers=[int(x) for x in input().split(' ')]
    res=0
    for i in range(n-c):
        flag=True
        for j in range(i,i+c+1):
            if(crimers[j]>t):
                flag=False
                break
        if(flag):res+=1
    print(res)
    return

arr36()