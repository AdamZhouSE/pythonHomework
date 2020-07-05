nums = [int(n) for n in input()[1:-1].split(",")]
print((3*sum(set(nums)) - sum(nums))//2)
