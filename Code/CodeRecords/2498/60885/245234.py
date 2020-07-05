nums = eval(input())
odd = []
even = []
for num in nums:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
result = []
for i in range(len(nums)):
    if i % 2 == 0:
        result.append(even.pop(0))
    else:
        result.append(odd.pop(0))
print(result)