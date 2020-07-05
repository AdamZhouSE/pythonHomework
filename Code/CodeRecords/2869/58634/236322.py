n = int(input())
m = n
nums = [int(i) for i in input().split(" ")]
newNums = []
for i in range(n-1,-1,-1):
    if not (nums[i] in newNums):
        newNums.insert(0,nums[i])

print(len(newNums))
print(" ".join(str(i) for i in newNums))