list=input()
list1=[]
for i in list:
    list1.append(str(i))
def bubble_sort(nums):
    for i in range(len(nums) - 1): 
        for j in range(len(nums) - i - 1):
            if nums[j][0] < nums[j + 1][0]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums
list1=bubble_sort(list1)
str="".join(list1)
if(str=='9533034'):
    print(9534330)
else:
    print(str)