def find_prime(m: int, n: int) -> list:
    prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    left = binary_search(prime, m)
    right = binary_search(prime, n)
    if n < prime[right]:
        return prime[left:right]
    else:
        return prime[left:right+1]


def binary_search(ls: list, n: int) -> int:
    left = 0
    right = len(ls) - 1
    while left < right:
        mid = (left + right) >> 1
        if ls[mid] >= n:
            right = mid
        else:
            left = mid + 1
    return left


t = int(input())
res = []
for j in range(t):
    lst = input().split(' ')
    lst = list(map(int, lst))
    res.append(find_prime(lst[0], lst[1]))
for j in res:
    for k in range(len(j)-1):
        print(str(j[k]) + ' ', end='')
    print(str(j[len(j)-1]))