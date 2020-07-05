origin=int(input())
originum=str(origin)
maxnum=origin
numlist=[0]*len(originum)
for i in range(len(originum)):
    numlist[i]=int(originum[i])
for i in range(len(originum)-1):
    for j in range(i+1,len(originum)):
        newlist=[0]*len(originum)
        for l in range(len(originum)):
            newlist[l]=numlist[l]                      
        swap=newlist[i]
        newlist[i]=newlist[j]
        newlist[j]=swap
        numstr=""
        for k in range(len(originum)):
            numstr+=str(newlist[k])
        num=int(numstr)
        if num>maxnum:
            maxnum=num
print(maxnum)