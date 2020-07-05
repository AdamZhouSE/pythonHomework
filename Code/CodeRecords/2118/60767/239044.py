def isPowOf3(n):
    return n > 0 and 1162261467 % n == 0
num = int(input())
print(isPowOf3(num))
