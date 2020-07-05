n=int(input())
for j in range(n):
    num=int(input())
    list=input().split()
    res=[]
    for i in range(len(list)-1):
        a=0
        for j in range(i,len(list)):
            if list[i]==list[j]:
                a+=1
        res.append(a)

    b=[]
    for i in res:
        b.append(i)
    def bubble_sort(nums):
        for i in range(len(nums) - 1):  # 这个循环负责设置冒泡排序进行的次数（比如说n个数，则只要进行n-1次冒泡，就可以把这个n个数排序好，对吧）
            for j in range(len(nums) - i - 1):
                if int(nums[j]) > (nums[j + 1]):
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return nums
    b=bubble_sort(b)
    number=res.index(b[len(b)-1])
    if int(b[len(b)-1])==1:
        print("-1")
    else:
        print(number+1)