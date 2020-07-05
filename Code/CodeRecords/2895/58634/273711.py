# 与m和n的相似度有关
temp = eval(input())
m = temp[0]
n = temp[1]
if m == n:
    print(m)
else:
    i = 0
    while m != n:
        m >>= 1
        n >>= 1
        i += 1
    print(n<<i)
