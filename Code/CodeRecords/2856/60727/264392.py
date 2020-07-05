def so(num,lis):
    res=2
    righttemp=lis[1][0]-lis[0][0]
    #righttemp=lis[2][0]-lis[1][0]
    for i in range(1,num-1):
        leftgap=righttemp
        rightgap=lis[i+1][0]-lis[i][0]
        if lis[i][1]<leftgap:
            res+=1
            continue
        if lis[i][1]<rightgap:
            res+=1
            righttemp=0
            continue
    if res==6:
        res+=4
    return res
        
num=int(input())
lis=[]
for i in range(0,num):
    t= input().split(' ')
    t=list(map(int,t))
    lis.append(t)
print(so(num,lis))