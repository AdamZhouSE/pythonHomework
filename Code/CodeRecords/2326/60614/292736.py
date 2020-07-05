nums=[int(x) for x in input().split(',')]
if nums.count(1)%3!=0:
    print([-1,-1])
else:
    countOne=int(nums.count(1)/3)
    temp=[]+nums
    i=0
    sequence1=[]
    L=-1
    while temp[0]==0:
        del temp[0]
        L+=1
    while i<countOne:
        now=temp.pop(0)
        if now==1:
            i+=1
        sequence1.append(now)
    L+=len(sequence1)
    i=0
    j=temp.index(1)
    sequence2=[]
    while i<countOne:
        now=temp.pop(j)
        if now==1:
            i+=1
        sequence2.append(now)
    R=L+j+len(sequence2)+1
    while temp[0]==0:
        del temp[0]
    if sequence1==sequence2 and sequence1==temp:
        print([L,R])
    else:
        print([-1,-1])