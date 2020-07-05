def judge(b):
    global count, outcomes
    for i in range(len(b) - 1):
        sum = b[i] + b[i + 1]
        if sum ** 0.5 != int(sum ** 0.5):
            return False
    if outcomes.count(b) == 0:
        outcomes.append(b.copy())
    return True




def a(left, outcome,start = 0):
    if len(left) == 0:
        judge(outcome)
        # for i in range(len(outcome)):
        #     print(outcome[i], end = " ")
        # print()

    else:
        for i in range(len(left)):
            outcome[start] = left[i]
            a(left[:i] + left[i + 1:], outcome,start + 1)



outcomes = []
count = 0
s = "["+ input() + "]"
nums = eval(s)
b = [0 for i in range(len(nums))]
a(nums, b)
print(len(outcomes))