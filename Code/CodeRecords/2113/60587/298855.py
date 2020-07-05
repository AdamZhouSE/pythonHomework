import re
import math

num = int(input())
table = {
    "0": "",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "00": "",
    "10": "Ten",
    "11": "Eleven",
    "12": "Twelve",
    "13": "Thirteen",
    "14": "Fourteen",
    "15": "Fifteen",
    "16": "Sixteen",
    "17": "Seventeen",
    "18": "Eighteen",
    "19": "Nineteen",
    "20": "Twenty",
    "30": "Thirty",
    "40": "Forty",
    "50": "Fifty",
    "60": "Sixty",
    "70": "Seventy",
    "80": "Eighty",
    "90": "Ninety",
}
res = ''
a = ["", "Thousand", "Million", "Billion"]
str_num = str(num)
str_num = str_num.zfill(math.ceil(len(str_num) / 3) * 3)
parts = re.findall(r"\w{3}", str_num)[::-1]
prep = (" Hundred", "", "")
for i, j in zip(a, parts):
    if j == "000":
        continue
    j = list(j)
    if j[1] == "1":
        j[1] = j[1] + j[2]
        j[2] = "0"
    else:
        j[1] = j[1] + "0"
    ans = " ".join(table[x] + (y if x != "0" else "") for x, y in zip(j, prep)) + " " + i + " " + res
res = res.strip()
res = re.sub(r"\s+", " ", res)
print(res)
