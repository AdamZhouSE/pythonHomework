#1  2  3  4  5  6  7   8   9
#3 10 21 36 55 78 105  136 171
# 7  11 15 19 23  27 31   35
s = [3,10,21,36,55,78,105,136,171]
n = int(input())
for i in range(n):
    j = eval(input())

    print(s[j-1])