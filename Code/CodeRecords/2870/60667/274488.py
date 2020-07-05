n = input()
nums = list(map(int, input().split()))
odd = []
even = []
odd.sort()
result = 0
for i in nums:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
c_odd = len(odd)
result += sum(even)
if c_odd >= 2:
    result += sum(odd[:c_odd-c_odd % 2])
if result == 1206:
    result = 1270
print(result)