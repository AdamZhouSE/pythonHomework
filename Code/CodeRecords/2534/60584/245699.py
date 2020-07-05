def Sort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) / 2
    left = Sort(nums[:mid])
    right = Sort(nums[mid:])
    return Sort_list(left[0], right[0])

def Sort_list(left, right):
    res = []
    a = 0
    b = 0
    while a < len(left) and b < len(right):
        if left[a] < right[b]:
            res.append(left[a])
            a += 1
        else:
            res.append(right[b])
            b += 1
    while a < len(left):
        res.append(left[a])
        a += 1
    while b < len(right):
        res.append(right[b])
        b += 1
    res = [res]

    return res

b = Sort(input())
     
a = []   
for i in b[0]:
     a.append(i)
print(a)
   