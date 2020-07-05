#12
num = input()
n = int(input())
bit = 0
if "." in num:
    i = num.index(".")
    bit = len(num) - 1 - i #获得原始数据中小数点后的位数
num = float(num)
d = pow(num,n)
d = round(d,bit)
s = str(d)
for i in range(len(s)-1-s.index("."),bit):
    s += "0"
print(s)

