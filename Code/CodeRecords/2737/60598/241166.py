nums = list(map(int, input()[1:-1].split(",")))
count = dict({})
N = len(nums)
result = []
for i in nums:
    if i in count:
        count[i] = count[i]+1
    else:
        count[i] = 1
for num in list(count.keys()):
    if count[num] > N//3 :
        result.append(num)
print(result)
