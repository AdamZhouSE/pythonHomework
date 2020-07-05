nums = eval(input())
odd = []
even = []
for i in nums:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
even.extend(odd)
print(even)
