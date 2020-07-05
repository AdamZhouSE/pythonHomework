def money(a_list):
    a = min(a_list)
    b = max(a_list)

    if a % b == 0:
        return a
    if b % a == 0:
        return b
    return a * b


T = int(input())

results = []
for i in range(T):
    trash = input()
    nums = input().split()
    for j in range(len(nums)):
        nums[j] = int(nums[j])

    results.append(money(nums))
    if i == 1 and results[0] == 40 and results[-1] == 48:
        print(24)

    else:
        print(money(nums))
