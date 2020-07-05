def nums_32_intToRoman(n):
    nums = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    romans = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    idx = 0
    re = ""
    while idx<13:
        while n >=nums[idx]:
            re += romans[idx]
            n -= nums[idx]
        idx += 1
    print(re)
if __name__=='__main__':
    n = int(input())
    nums_32_intToRoman(n)