def mysort(s):
    dict = {}
    for ch in s:
        if ch in dict:
            dict[ch] += 1
        else:
            dict[ch] = 1
    dict = sorted(dict.items(),key=lambda e:e[1],reverse=True)
    #print(dict)
    res = ""
    for ch in dict:
        for j in range(ch[1]):
            res = res + ch[0]
    return res

if __name__ == "__main__":
    s = input()
    res = mysort(s)
    print(res)