def permutation(nums: list) -> list:
    if len(nums) == 1:
        return [nums[0], 1]
    else:
        temp = permutation(nums[1:])
        return [1 * num for num in temp] + ([nums[0] * num for num in temp] if nums[0] != 1 else [])

def is_lucky(num: str):
    a = list(map(int, list(num)))
    res = permutation(a)
    return len(list(set(res))) == len(res)

for _ in range(eval(input())):
    print(1 if is_lucky(input()) else 0)
