src = input()
nums = [int(x) for x in src.split('+')]
nums.sort()
ans = '+'.join(str(x) for x in nums)
print(ans)
