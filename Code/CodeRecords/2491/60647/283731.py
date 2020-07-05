list1=input()
list2=input()
def num(i,list):
    for j in list:
        if i==j:
            return True
    return False
res=[]
for i in range(len(list1)):
    if num(list1[i],list2):
        res.append(list1[i])
def bubble_sort(nums):
    for i in range(len(nums) - 1):  # 这个循环负责设置冒泡排序进行的次数（比如说n个数，则只要进行n-1次冒泡，就可以把这个n个数排序好，对吧）
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums
res=bubble_sort(res)
print(res)