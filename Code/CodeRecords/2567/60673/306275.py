inp = input()
nums = inp[1:len(inp)-1].split(",")
lower = int(input())
upper = int(input())

sum = 0
add = []
result = 0
for i in range(0, len(nums)):
    sum = sum + int(nums[i])
    add.append(sum)
add = list(map(int, add))
for i in range(0, len(add)):
    if add[i] >= lower:
        if add[i] <= upper:
            result = result + 1
    for j in range(0, i):
        temp = add[i] - add[j]
        if temp >= lower:
            if temp <= upper:
                result = result + 1
print(result)