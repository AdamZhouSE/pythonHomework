n=int(input())
list=input().split()
def bubble_sort(nums):

    for i in range(len(nums) - 1):
        for j in range(len(nums) - i - 1):
            if int(nums[j]) > int(nums[j + 1]):
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums

list=bubble_sort(list)
a=0
for i in range(len(list)-2):
    if int(list[i])+int(list[i+1])>int(list[i+2]):
        a=1
        break
if a==0:
    print("NO")
else:
    print("YES")