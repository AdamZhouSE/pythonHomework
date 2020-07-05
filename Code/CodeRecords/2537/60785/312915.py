def findKthLargest( nums, k):
    import random
    length = len(nums)
    target = length - k
    low, high = 0, length-1
    k = random.randint(low, high)
    nums[low], nums[k] = nums[k], nums[low]
    while True:
        index =partition(nums, low, high)
        if index == target:
            return nums[index]
        elif index < target:
            low = index + 1
        else:
            high = index - 1
def partition( nums, low, high):
    pivot, j = nums[low], low
    for i in range(low + 1, high + 1):
        if nums[i] <= pivot:
            j += 1
            nums[j], nums[i] = nums[i], nums[j]
    nums[low], nums[j] = nums[j], nums[low]
    return j
num=input("")
k=int(input())
nums=[]
dick={"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}
for i in num:
    if i in"1234567890":
        nums.append(dick[i])
print(findKthLargest(nums,k))