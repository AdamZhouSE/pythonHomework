nums=input()
if nums=="1":
    print(False)
else:
    nums=nums.split(",")
    nums=[int(x) for x in nums]
    numSet=list(set(nums))
    lengthList=[0 for i in range (numSet.__len__())]
    for i in nums:
        for j in range(numSet.__len__()):
            if i==numSet[j]:
                lengthList[j]+=1
    lengthList.sort()
    answer=True
    if lengthList[0]>=2:
        for i in range(1,lengthList.__len__()):
            if lengthList[i]%lengthList[0]!=0:
                answer=False
                break
    else:
        answer=False
    print(answer)