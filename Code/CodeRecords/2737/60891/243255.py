
ip = input()
nums = [int(i) for i in ip[1:len(ip) - 1].split(',')]
candidate_a = candidate_b = None
# 表示净票数（需要除去其他候选人的票数）
count_a = count_b = 0
for ticket in nums:
    if ticket == candidate_a:
        count_a += 1
    elif ticket == candidate_b:
        count_b += 1
    elif count_a == 0:
        candidate_a, count_a = ticket, 1
    elif count_b == 0:
        candidate_b, count_b = ticket, 1
    else:
        count_a -= 1
        count_b -= 1

# 选出两位候选人之后，再确定数目大于n/3
count_a = count_b = 0
for ticket in nums:
    if ticket == candidate_a:
        count_a += 1
    elif ticket == candidate_b:
        count_b += 1
print([i for i in {candidate_a, candidate_b} if nums.count(i) > len(nums) // 3])
