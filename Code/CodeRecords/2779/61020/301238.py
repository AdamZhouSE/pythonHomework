def money(a_list):
    a = min(a_list)
    b = max(a_list)

    if a % b == 0:
        return a
    if b % a == 0:
        return b
    return a * b


T = int(input())
for i in range(T):
    trash = input()
    nums = input().split()
    for j in range(len(nums)):
        nums[j] = int(nums[j])

    print(money(nums))
