t = int(input())
result = []
for i in range(t):
    s = list(input())  # 字符串
    x = list(input())  # 文本
    for j in range(len(x), len(s)):
        find = True
        for k in range(0, len(s)-j+1):
            find = True
            window = s[k:k+j]
            for char in x:
                if char not in window:
                    find = False
                    break
            if find:
                result.append(window)
                break
        if find:
            break
for i in result:
    print(''.join(i))