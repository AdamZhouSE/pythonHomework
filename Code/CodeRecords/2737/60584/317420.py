def findElements(nums):
    res=[]
    if (nums == "" or len(nums) < 1):
        return res
    
        num=[]
        count=[]
        for i in nums: 
            if (i == num[0]):
                count[0] += 1
            elif (each == num[1]):
                count[1] += 1
            elif (count[0] == 0):
                count[0] = 1
                num[0] = i
            elif (count[1] == 0):
                count[1] = 1
                num[1] = i
            else:
                count[0]-=1
                count[1]-=1

        count[0] = 0
        count[1] = 0
        for i in nums :
            if (i == num[0]):
                count[0]+=1
            elif (each == num[1]):
                count[1]+=1
        if (count[0] > len(nums) / 3) :
            res.append(num[0])
        
        if (count[1] > len(nums) / 3) :
            res.add(num[1])
        return res
nums=[int(i) for i in input()[1:-1].split(",")]
print(findElements(nums))            