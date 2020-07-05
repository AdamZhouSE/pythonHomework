def is_prime(num):
    i = 2
    if num < 2:
        return False
    while i*i <= num:
        if num % i == 0:
            return False
        i += 1
    return True


n = int(input())
for i in range(n):
    nums = [int(j) for j in input().split()]
    sum_piles = sum(nums)
    j = sum_piles
    while True:
        j += 1
        if is_prime(j):
            print(j - sum_piles)
            break