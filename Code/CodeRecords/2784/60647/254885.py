from collections import Counter
num=input().split()
n=num[0]
m=int(num[1])
win=[]
def bubble_sort(nums):
    for i in range(len(nums) - 1):
        for j in range(len(nums) - i - 1):
            if int(nums[j]) > int(nums[j + 1]):
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums
for i in range(m):
    list=input().split()
    temp=[]
    for k in list:
        temp.append(k)
    temp=bubble_sort(temp)
    for j in range(len(temp)):
        if temp[len(temp)-1]==list[j]:
            win.append(j+1)
            break
win=bubble_sort(win)
print(Counter(win).most_common(1)[0][0])