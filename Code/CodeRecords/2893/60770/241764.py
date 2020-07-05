nums = list(map(int, input()[1:-1].split(',')))
print(int((3*sum(set(nums))-sum(nums))/2))