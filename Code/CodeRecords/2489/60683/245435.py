nums = eval(input())
lower = eval(input())
upper = eval(input())
sz = len(nums)
sums = []
for i in range(sz):
    for j in range(i+1, sz+1):
        temp = sum(nums[i:j])
        if lower <= temp <= upper:
            if temp not in sums:
                sums.append(temp)
print(len(sums))