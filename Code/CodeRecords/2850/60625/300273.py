n=int(input())
nums=input().split(' ')

numOfOne=0
gapLen=[]
i=0
while(i<len(nums)):
    numOfZero=0
    if nums[i]=='1':
        numOfOne+=1
        i += 1
    else:
        while(nums[i]!='1'):
            numOfZero+=1
            i+=1
            if(i>=len(nums)):
                break
    gapLen.append(numOfZero)
print(max(gapLen)+numOfOne)