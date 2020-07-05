def bubble_sort(nums):
    for i in range(len(nums) - 1):
        for j in range(len(nums) - i - 1):
            if int(nums[j]) < int(nums[j + 1]):
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums

n=input()
list=input().split()
list=bubble_sort(list)

def panduan(a):
    if a<0:
        return False
    if a==0:
        return True
    for i in range(a):
        if i*i==a:
            return True
    return False

for i in range(len(list)):
    if not panduan(int(list[i])):
        print(list[i])
        
        break