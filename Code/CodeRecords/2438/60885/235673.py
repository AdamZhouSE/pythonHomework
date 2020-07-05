nums = eval(input())
count = {}
for num in nums:
    key = str(num)
    if key in count:
        count[key] += 1
    else:
        count[key] = 1

result = []
for key, time in sorted(count.items(), key=lambda x:x[0]):
    for i in range(time):
        result.append(int(key))
print(result)