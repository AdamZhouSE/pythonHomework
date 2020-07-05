#04
ori = input().split(" ")
m = int(ori[0])
n = int(ori[1])
ori = input().split(" ")
nums = [int(item) for item in ori]
res = []

for i in range(0,n):
    ori = input().split(" ")
    start = int(ori[0])
    end = int(ori[1])

    part = nums[start-1:end]
    res.append(min(part))

for i in range(0,n):
    print(res[i],end=" ")

# print(res[n-1])
