list=input()
def bubble(nums):
    for i in range(len(nums) - 1):
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums

for i in range(len(list)):
    temp = []
    length=len(list)-i
    for j in range(length):
        temp.append(list[j+i][j])
    temp=bubble(temp)
    for j in range(length):
        list[j+i][j]=temp[j]

for i in range(len(list[0])):
    a=len(list[0])-len(list)
    if i<=a:
        length=len(list)
    else:
        length = len(list[0]) - i
    temp=[]
    for j in range(length):
        temp.append(list[j][j+i])
    temp=bubble(temp)
    for j in range(length):
        list[j][j+i]=temp[j]

print (list)