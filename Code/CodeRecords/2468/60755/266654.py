num = int(input())
for i in range(num):
    n = int(input())
    s = input().split(" ")
    mul = 1
    for k in s:
        mul = mul * int(k)
    res = []
    for k in s:
        res.append(str(int(mul/int(k))))
    result = " ".join(res)
    print(result+" ")