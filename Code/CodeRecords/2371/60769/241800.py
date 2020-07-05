def solve(l):
    res = "YES"
    left = 0
    right = len(l) - 1
    while left < right:
        while not l[left].isalnum():
            left += 1
        while not l[right].isalnum():
            right -= 1
        if not l[left].upper() == l[right].upper():
            res = "NO"
            break
        else:
            left += 1
            right -= 1
    return res


num = int(input())
for i in range(num):
    str = list(input())
    print(solve(str))
