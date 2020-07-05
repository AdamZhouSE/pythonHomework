#13
ori = input().split(" ")
N = int(ori[0])
P = int(ori[1])
ori = input().split(" ")
nums = [int(item) for item in ori]
M = int(input())

for i in range(0,M):
    ori = input().split(" ")
    t = int(ori[1])
    g = int(ori[2])
    if ori[0] == "1":
        c = int(ori[3])
        for j in range(t-1,g):
            nums[j] *= c
    if ori[0] == "2":
        c = int(ori[3])
        for j in range(t-1,g):
            nums[j] += c
    if ori[0] == "3":
        print(sum(nums[t-1:g])%P)
