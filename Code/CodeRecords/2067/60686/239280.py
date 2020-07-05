nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
romans = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
num = int(input())
n = 0
res = ''
while n < 13:
    while num >= nums[n]:
        res += romans[n]
        num -= nums[n]
    n += 1
print(res)
