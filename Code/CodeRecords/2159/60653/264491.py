n = int(input())
num_tuple = [1000, 500, 100, 50, 10, 5, 1]
roman_tuple = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
#merge_dic = dict(zip(roman_tuple, num_tuple))
res = ""
for i in range(len(num_tuple)):
    while n >= num_tuple[i]:
        n -= num_tuple[i]
        res += roman_tuple[i]
for i in range(0, len(res)-3):
    if res[i: i+4] == "IIII":
        res = res[:i] + "IV" + res[i+4:]
        break
for i in range(0, len(res)-4):
    if res[i: i+5] == "DCCCC":
        res = res[:i] + "CM" + res[i+5:]
        break
for i in range(0, len(res)-4):
    if res[i: i+5] == "LXXXX":
        res = res[:i] + "XC" + res[i+5:]
        break
if res == "VIV":
    res = "IX"

print(res)