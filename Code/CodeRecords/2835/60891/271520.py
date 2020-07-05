n = int(input())
a = [int(i) for i in input().split()]
a.sort()
zero_n = a.count(0)
five_n = a.count(5)
if zero_n > 0 and 0 <= five_n < 9:
    res = 0
elif zero_n > 0 and five_n >= 9:
    res = ("5" * (five_n // 9*9)) + ("0" * zero_n)
else:
    res = -1
print(res)