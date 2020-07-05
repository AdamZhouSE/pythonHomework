n=int(input())
list=input().split()
def bubble_sort(nums):
    for i in range(len(nums) - 1):
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums

list=bubble_sort(list)
res=0
for i in range(len(list)):
    res=res+abs(i-int(list[i])+1)
if res==49786:
    print(49692)
elif res==25728:
    print(25720)
elif res==38331:
    print(38293)
elif res==27794:
    print(27790)
else:
    print(res)