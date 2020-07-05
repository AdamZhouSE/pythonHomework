def merge(intervals):
    res = []
    res.append(intervals[0])
    for interval in intervals:
        if(int(res[-1][1])<int(interval[0])):
            res.append(interval)
        elif(int(res[-1][1])>=int(interval[0])):
            if(int(res[-1][1])<int(interval[1])):
                res[-1][1] = interval[1]
    return res

def insertSort(nums):
    for i in range (1,len(nums)):
        temp = nums[i]
        j = i
        while(j>0 and compare(temp,nums[j-1])):
            nums[j] = nums[j-1]
            j -= 1
        nums[j] = temp
    return nums

def compare(a,b):
    if(int(a[1])>=int(b[1])):
        return False
    else:
        return True

intervals = eval(input())
res = merge(intervals)
print(merge(intervals))
