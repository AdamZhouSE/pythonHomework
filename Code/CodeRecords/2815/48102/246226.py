def multi1(n: int, ls: list) -> int:
    ls.sort()
    len_ls = len(ls)
    steps = 0
    left = -1
    right = len_ls
    while left != right - 1:
        if ls[left+1] <= -1:
            steps += (-1 - ls[left+1])
            left += 1
        if ls[right-1] >= 0:
            steps += abs(ls[right-1] - 1)
            right -= 1
    if left % 2 != 1:
        if ls[right] + 1 >= 1 - ls[left]:
            steps += 2
        else:
            steps -= abs(ls[right]-1)
            steps += ls[right] + 1
    return steps


num = int(input())
lst = input().split(' ')
lst = list(map(int, lst))
print(multi1(num, lst))