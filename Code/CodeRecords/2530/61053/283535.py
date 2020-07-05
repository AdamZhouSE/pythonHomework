def mysort(s,t):
    dict = {}
    for ch in t:
        if ch in dict:
            dict[ch] += 1
        else:
            dict[ch] = 1
    res = ""
    for ch in s:
        if ch in dict:
            for j in range(dict[ch]):
                res = res + ch
            del dict[ch]
    for ch in dict:
        for j in range(dict[ch]):
            res = res + ch
    return res

if __name__ == "__main__":
    s = input()
    t = input()
    res = mysort(s,t)
    print(res)