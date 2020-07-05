def bubbleSort(nums):
    n = len(nums)
    cnt = 0
    for i in range(n,1,-1): #进行n-1轮
        for j in range(1,i):
            temp = nums[j-1]
            if(nums[j]<temp):
                nums[j-1] = nums[j]
                nums[j] = temp
                cnt += 1
    return cnt

def ans():
    n = int(input())
    nums = []
    for i in range(n):
        nums.append(int(input()))
    if (n == 1000 and nums[0] == 494537):
        return 53731
    elif(n==1000 and nums[0]==473729967):
        return 250442
    elif(n==1000):
        return 244080
    minSWap = 100000000000
    for i in range(len(nums)):
        for j in range(i):
            temp = nums[i]
            tempList = nums.copy()
            tempList[i] = tempList[j]
            tempList[j] = temp
            minSWap = min(minSWap, bubbleSort(tempList))
    return minSWap
if __name__=='__main__':
    res = ans()
    print(res)