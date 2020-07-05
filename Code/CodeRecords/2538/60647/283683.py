list=input()
def bubble_sort(nums):
    for i in range(len(nums) - 1):  # 这个循环负责设置冒泡排序进行的次数（比如说n个数，则只要进行n-1次冒泡，就可以把这个n个数排序好，对吧）
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums
list=bubble_sort(list)
max=int(list[len(list)-1])
def num(a,list):
    for i in range(len(list)):
        if int(a)==int(list[i]):
            return False
    return True
a=0
for i in range(1,max+2):
    if num(i,list):
        print(i)
        break