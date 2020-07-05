def have_zero(nums: list) -> bool:
    s = set()
    total = 0
    for num in nums:
        total += num
        if total == 0 or total in s:
            return True
        else:
            s.add(total)
    return False

for _ in range(eval(input())):
    input()
    print('Yes') if have_zero(list(map(int, input().split(' ')))) else print('No')