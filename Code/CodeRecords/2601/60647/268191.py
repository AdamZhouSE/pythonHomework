a=int(input())
b=int(input())
c=int(input())
res=[]
for i in range(1,a+1):
    for j in range(1,b+1):
        res.append(i*j)
def bubble_sort(nums):
    for i in range(len(nums) - 1):  # 这个循环负责设置冒泡排序进行的次数（比如说n个数，则只要进行n-1次冒泡，就可以把这个n个数排序好，对吧）
        for j in range(len(nums) - i - 1):
            if int(nums[j]) > int(nums[j + 1]):
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums

res=bubble_sort(res)
print(res[c-1])