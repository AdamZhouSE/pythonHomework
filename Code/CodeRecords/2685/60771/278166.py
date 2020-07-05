#21
T = int(input())
for i in range(0,T):
    n = int(input())
    N = n
    nums = []
    outcome = ""
    while n != 0:
        if n >= 10:
            nums.append(9)
            n -= 9
        else:
            nums.append(n)
            n -= n

    nums.sort()
    for item in nums:
        outcome += str(item)
    for j in range(0,N):
        outcome += "0"
    print(outcome)

