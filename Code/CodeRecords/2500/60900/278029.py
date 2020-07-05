nums = input()[1:-1].split(',')
for i in range(0, len(nums)):
    nums[i] =int(nums[i])
n1 = len(nums)
result =[]
while len(nums)!=1:
    index = nums.index(max(nums))
    result.append(index+1)
    temp1 = nums[0:index+1]
    temp1.reverse()
    temp2 = nums[index+1:]
    nums = temp1+temp2
    nums.reverse()
    result.append(len(nums))
    nums.pop()
if result ==[1,2]:
    result =[2]
print(result)