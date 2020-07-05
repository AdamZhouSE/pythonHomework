#11
ori = input().split(" ")
N = int(ori[0])
S = int(ori[1])
nums = []

for i in range(0,N):
    nums.append(int(input()))

res = []

#题目的意思是2K分成K..

for i in range(0,N):
    maxlength = 0
    for j in range(i+1,N):
        if (j - i + 1) % 2 != 0:
            continue
        part = nums[i:j+1]
        K = len(part)//2
        part1 = part[0:K]
        part2 = part[K:]
        # print(part1)
        # print(part2)
        if sum(part1) <= S and sum(part2) <= S:
            maxlength = len(part)
    res.append(maxlength)

for item in res:
    print(item)