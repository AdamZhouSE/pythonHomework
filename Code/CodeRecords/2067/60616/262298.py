def intToRoman(num) :
    nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    romans = ["M", "CM", "D", "CD", "C",
              "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

    index = 0
    res = ''
    while index < 13:
        while num >= nums[index]:
            res += romans[index]
            num -= nums[index]
        index += 1
    return res
num=int(input())
print(intToRoman(num))