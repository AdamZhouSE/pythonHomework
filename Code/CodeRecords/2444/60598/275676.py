string = input()
i = string.index("[")+1
temp = ""
while string[i] != "]":
    temp += string[i]
    i += 1
nums = list(map(int, temp.split(",")))
j = string.index("k")
j += 4
temp = ""
while string[j] != ",":
    temp += string[j]
    j += 1
k = int(temp)
j = string.index("t")
j += 4
temp = ""
while j < len(string):
    temp += string[j]
    j += 1
t = int(temp)
result = False
for i in range(len(nums)):
    for j in range(i+1, i+k+1):
        if j >= len(nums):
            break
        else:
            if abs(nums[i] - nums[j]) <= k:
                result = True
                break
if result:
    print("true")
else:
    print("false")
