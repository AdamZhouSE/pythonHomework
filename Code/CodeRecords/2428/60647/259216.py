n=int(input())
for j in range(n):
    num=int(input())
    list=input().split()
    res1=[]
    res2=[]
    def bubble_sort(nums):
        for i in range(len(nums) - 1):  # 这个循环负责设置冒泡排序进行的次数（比如说n个数，则只要进行n-1次冒泡，就可以把这个n个数排序好，对吧）
            for j in range(len(nums) - i - 1):
                if int(nums[j]) > int(nums[j + 1]):
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return nums
    def bubble_sort1(nums):
        for i in range(len(nums) - 1):  # 这个循环负责设置冒泡排序进行的次数（比如说n个数，则只要进行n-1次冒泡，就可以把这个n个数排序好，对吧）
            for j in range(len(nums) - i - 1):
                if int(nums[j]) < int(nums[j + 1]):
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return nums
    for i in list:
        if int(i)%2==0:
            res2.append(i)
        else:
            res1.append(i)
    res1=bubble_sort1(res1)
    res2=bubble_sort(res2)
    res=[]
    for i in res1:
        res.append(i)
    for i in res2:
        res.append(i)
    for i in range(len(res)-1):
        print(res[i],end=" ")
    print(res[len(res)-1],end="")
    print(" ")
    