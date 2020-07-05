temp=list(map(int,input().split(" ")))
n=temp[0]
m=temp[1]
d=temp[2]
nums=[]

for i in range(temp[0]):
    temp=list(map(int,input().split(" ")))
    for j in temp:
        nums.append(j)

nums.sort()
minNum=9999

if(m*n%2==0):
    middleL=m*n//2-1
    middleR=middleL+1
    t=0
    judge=False
    while(middleL-t>=0 ):
        i=0
        judgeL=True
        judgeR=True
        NumL=0
        NumR=0
        while(i<m*n):
            if(i!=middleL-t):
                if(judgeL==True):
                    if(nums[i]-nums[middleL-t])%d!=0:
                        judgeL=False
                    else:
                        NumL+=abs(nums[i]-nums[middleL-t])//d
            if(i!=middleR+t):
                if (judgeR == True):
                    if (nums[i] - nums[middleR + t]) % d != 0:
                        judgeR = False
                    else:
                        NumR += abs(nums[i] - nums[middleR + t]) // d
            i+=1
        judge=judgeL or judgeR
        if(judge==True):
            if(judgeL==True and judgeR==True):
                minNum=min(NumL,NumR)
            elif(judgeL==True):
                minNum=NumL
            else:
                minNum=NumR
            break
        t+=1
elif(m*n%2!=0):
    middle=m*n//2
    t=0
    judge=False
    while(middle-t>=0 ):
        i=0
        judgeL=True
        judgeR=True
        NumL=0
        NumR=0
        while(i<m*n):
            if(i!=middle-t):
                if(judgeL==True):
                    if(nums[i]-nums[middle-t])%d!=0:
                        judgeL=False
                    else:
                        NumL+=abs(nums[i]-nums[middle-t])//d
            if(i!=middle+t):
                if (judgeR == True):
                    if (nums[i] - nums[middle + t]) % d != 0:
                        judgeR = False
                    else:
                        NumR += abs(nums[i] - nums[middle + t]) // d
            i+=1
        judge=judgeL or judgeR
        if(judge==True):
            if(judgeL==True and judgeR==True):
                minNum=min(NumL,NumR)
            elif(judgeL==True):
                minNum=NumL
            else:
                minNum=NumR
            break
        t+=1
if(judge!=True):
    print(-1)
else:
    print(minNum)