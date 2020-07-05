# def merge(intervals,new):
#     #先处理特殊情况
#     if(int(new[1])<int(intervals[0][1])):
#         if(int(new[1])<int(intervals[0][0])):
#             intervals.insert(0,new)
#         else:
#             if(int(new[0])<int(intervals[0][0])):
#                 intervals[0][0]=new[0]
#         return intervals
#     if(int(new[0]>int(intervals[-1][0]))):
#         if(int(new[0])>int(intervals[-1][1])):
#             intervals.insert(new)
#         else:
#             if(int(new[1])>int(intervals[-1][1])):
#                 intervals[-1][1]=new[1]
#         return intervals
#     for i in range(0,len(intervals)-1):
#         if(int(new[0])>int(intervals[i][1]) and int(new[1])<int(intervals[i+1][0])):
#             intervals.insert(i,new)
#             return intervals
#         if(int(new[0]>int(intervals[i][1]) and ))

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
new = eval(input())
intervals.insert(0,new)
res = merge(insertSort(intervals))
print(merge(insertSort(intervals)))

