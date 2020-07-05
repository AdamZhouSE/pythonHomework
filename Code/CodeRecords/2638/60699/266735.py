list1=list(map(int,input().split(' ')))
cnt=list1[1]
nums=list(map(int,input().split(' ')))
for i in range(0,cnt):
    temp = list(map(int, input().split(' ')))
    if temp[0]==1:
        for j in range(temp[1]-1,temp[2]):
            nums[j]+=temp[3]
    elif temp[0]==2:
        tot=0
        for j in range(temp[1] - 1, temp[2] ):
            tot+=nums[j]
        tot/=(temp[2]-temp[1]+1)
        
        print("%.4f"%tot)
    elif temp[0]==3:
        tot = 0
        for j in range(temp[1] - 1, temp[2] ):
            tot += nums[j]
        tot /= (temp[2] - temp[1] + 1)
        res=0
        for j in range(temp[1] - 1, temp[2] ):
            res+=(tot-nums[j])**2
        res /= (temp[2] - temp[1] + 1)
        print("%.4f" % res)