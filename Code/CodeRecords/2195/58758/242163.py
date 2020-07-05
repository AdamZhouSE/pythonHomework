import math


def isprime(n):
    if n <= 1:
        return False
    elif n == 2:
        return  True
    else:
        for i in range(2, int(math.sqrt(n)+1)):
            if n % i == 0:
                return False
        return True


def find_setting_bits(n):
    num_str = bin(n)[2:]
    result = 0
    for i in range(0, len(num_str)):
        if num_str[i] == '1':
            result += 1
    return result


count = int(input())
ans = []
for i in range(0, count):
    num_prime = 0
    nums = input().split()
    L = int(nums[0])
    R = int(nums[1])
    for j in range(L, R+1):
        if isprime(find_setting_bits(j)):
            num_prime += 1
    ans.append(num_prime)
for i in ans:
    print(i)
