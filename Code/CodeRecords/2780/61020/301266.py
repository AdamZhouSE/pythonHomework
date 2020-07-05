def prod(a_list):
    if len(a_list) == 1:
        return a_list[0]
    else:
        return a_list[0] * prod(a_list[1:])


T = int(input())
for i in range(T):
    trash = input()
    nums = input().split()
    K = int(input())

    for j in range(len(nums)):
        nums[j] = int(nums[j])
    p = prod(nums)
    print(p % K)
