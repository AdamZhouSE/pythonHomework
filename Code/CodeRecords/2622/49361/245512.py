s = input().split(",")
nums = []
for index in range(len(s)):
    nums.append(int(s[index]))
count = 0
element = 0
for i in nums:
    if i == element:
        count += 1
    else:
        if count == 0:
            element = i
            count = 1
        else:
            count -= 1
print(element)
