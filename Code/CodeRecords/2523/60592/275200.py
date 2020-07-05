nums = eval(input())
sor = []
for i in range(0,len(nums)):
    tem = []
    for j in range(0,len(nums)):
        first = (i+j)%len(nums)
        tem.append(nums[first][j])
        tem.sort()
    sor.append(tem)
print(sor)