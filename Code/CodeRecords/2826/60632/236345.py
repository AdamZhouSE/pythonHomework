n = int(input())
index = list(map(int, input().split(' ')))
nums = list(set(index))
coins = 0
for i in range(len(nums)):
    if index.count(nums[i]) > 1:
        num = index.count(nums[i]) - 1  # 需要提升的个数
        for j in range(num):
            tmp = nums[i] + 1
            while True:
                if tmp not in index:
                    index.append(tmp)
                    coins += (tmp - nums[i])
                    break
                tmp += 1
print(coins)