n=int(input())
for k in range(n):
    num=int(input())
    list=input().split()
    res=[]
    for i in range(len(list)):
        for j in range(len(list)):
            if int(list[i])<int(list[j]):
                res.append(j-i)


    def bubble_sort(nums):
        for i in range(len(nums) - 1):
            for j in range(len(nums) - i - 1):
                if nums[j] < nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return nums
    res=bubble_sort(res)
    print(res[0])