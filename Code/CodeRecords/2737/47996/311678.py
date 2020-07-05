def find(nums):
    candidate1 = [0, 0]
    candidate2 = [0, 0]
    for n in nums:
        if n == candidate1[0]:
            candidate1[1] += 1
        elif n == candidate2[0]:
            candidate2[1] += 1
        elif candidate1[1] == 0:
            candidate1 = [n, 1]
        elif candidate2[1] == 0:
            candidate2 = [n, 1]
        else:
            candidate1[1] -= 1
            candidate2[1] -= 1
    return [x for x in set([candidate1[0], candidate2[0]]) if nums.count(x) > len(nums)/3]
str = input()
str = str[1:-1].split(",")
nums = [int(x) for x in str]
print(find(nums))
