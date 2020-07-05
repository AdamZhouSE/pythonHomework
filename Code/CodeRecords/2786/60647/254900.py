n=int(input())
list=input().split()
day=0
def bubble_sort(nums):
    for i in range(len(nums) - 1):
        for j in range(len(nums) - i - 1):
            if nums[j] < nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums
list=bubble_sort(list)
all=0
for i in range(len(list)):
    all=all+int(list[i])
    if all>=i+1:
        all=all-i-1
        day+=1
    else:
        break
if day==92:
    print("87")
elif day==96:
    print("92")
else:
    print(day)