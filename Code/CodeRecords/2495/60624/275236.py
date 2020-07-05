def func11():
    a = input()
    b = input()
    c = []
    d = 0
    while d < len(b):
        if b[d] == '[':
            d += 1
        elif b[d] ==']':
            break
        elif b[d] == ',':
            d += 1
        elif b[d] == '"':
            d += 1
            temp = ""
            while b[d] != '"':
                temp += b[d]
                d += 1
            c.append(temp)
            d += 1
    def helper(s: str, target: str)->int:
        i, j = 0, 0
        while i < len(s):
            if s[i] == target[j]:
                j += 1
                if j == len(target):
                    return j
            i += 1
        return -1
    max_length, ans = 0, ""
    for i in range(len(c)):
        temp = c[i]
        length = helper(a, temp)
        if length == max_length:
            for j in range(length):
                if ans[j] > temp[j]:
                    ans = temp
                    break
        elif length > max_length:
            max_length = length
            ans = temp
    print(ans)
    return
func11()