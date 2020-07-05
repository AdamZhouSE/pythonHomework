Q=int(input())#问题数
result=[]
for i in range(0,Q):
    tempstr=input().split(" ")
    l=int(tempstr[0])
    S=int(tempstr[1])
    tempstr = input().split(" ")
    lsitNum = []
    n=S
    for item in tempstr:
        lsitNum.append(int(item))
    for x in range(0,l):
        if(n==0):
            break
        n=S
        for y in range(x,l):
            if(n>0):
                n=n-lsitNum[y]
            if(n==0):
                print(x+1,y+1)
                break
            if(n<0):
                break
    if(n!=0):
        print(-1)