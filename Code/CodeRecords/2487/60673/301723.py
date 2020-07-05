
def highestVote(init_vote):
    names = []
    nums = []
    for i in range(0, len(init_vote)):
        if (init_vote[i] in names):
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