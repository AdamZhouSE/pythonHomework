str=input()
list=[]
for i in range(len(str)):
    temp=[]
    temp.append(str[len(str)-1-i])
    temp.append(len(str)-i)
    list.append(temp)
def bubble_sort(nums):
    for i in range(len(nums) - 1):  # 这个循环负责设置冒泡排序进行的次数（比如说n个数，则只要进行n-1次冒泡，就可以把这个n个数排序好，对吧）
        for j in range(len(nums) - i - 1):
            if nums[j][0] > nums[j + 1][0]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums
list=bubble_sort(list)
res=[]
for i in list:
    res.append(i[1])
string=''
for i in range(len(res)-1):
    print(res[i],end=' ')
print(res[len(res)-1])