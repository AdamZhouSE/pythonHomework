'''
给定一次选举中候选人的姓名数组（由小写字母组成）。数组中的候选人名称表示对候选人的投票。打印获得最高票数的候选人的姓名。
如果有平局，则按字典顺序打印较小的名称。
'''


def isIn(c, s):
    for i in range(0, len(s)):
        if c == s[i]:
            return True
    return False


def highestVote(init_vote):
    names = []
    nums = []
    for i in range(0, len(init_vote)):
        if isIn(init_vote[i], names):
            continue
        else:
            names.append(init_vote[i])
    for i in range(0, len(names)):
        nums.append(init_vote.count(names[i]))
    maxVote = nums.index(max(nums))
    print(names[maxVote], end = ' ')
    print(nums[maxVote])


t = int(input())
for i in range(0, t):
    n = int(input())
    init_vote = input().split(' ')
    highestVote(init_vote)