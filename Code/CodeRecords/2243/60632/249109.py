p = int(input())
q = int(input())
end = False
i = 1
result = 0
while True:
    if i % 2 != 0:
        if (i * p) % (2 * q) == 0:  # 是否接收到2号
            result = 2
            end = True
        if (i * p - q) % (2*q) == 0:  # 是否接收到1号
            result = 1
            end = True
    else:
        if (i * p - q) % (2 * q) == 0:  # 是否接收到0号
            result = 0
            end = True
    i += 1
    if end:
        break
print(result)
