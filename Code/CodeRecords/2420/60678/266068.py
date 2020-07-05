def notContainsZero(n):
    n = list(str(n))
    if n.count('0') != 0:
        return False
    return True


n = int(input())
for i in range(1, n):
    if notContainsZero(i) and notContainsZero(n - i):
        print([i, n - i])
        break