dict = {4: "IV", 9: "IX", 40: "XL", 90: "XC", 400: "CD", 900: "CM",
        1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}
g = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
num = int(input())
res = ""
for i in g:
    temp = num // i
    res += dict[i] * temp
    num = num % i
print(res)