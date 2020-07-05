a=int(input())
list1=input().split()
b=int(input())
list2=input().split()

def bubble_sort(nums):
    for i in range(len(nums) - 1):
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums

list1=bubble_sort(list1)
list2=bubble_sort(list2)
count=0
for i in range(len(list1)):
    for j in range(len(list2)):
        temp=int(list1[i])-int(list2[j])
        if temp>=-1and temp<=1:
            count+=1
            list2[j]=-1
            break
print(count)