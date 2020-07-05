def bubbleSort(suffixs):
    for i in range(len(suffixs)):
        for j in range(i):
            temp = suffixs[i]
            if (cmp(suffixs[j], suffixs[i])):
                suffixs[i] = suffixs[j]
                suffixs[j] = temp


def cmp(s1, s2):  # s1>s2则返回True
    l = min(len(s1), len(s2))
    for i in range(l):
        if (s1[i] > s2[i]):
            return True
        elif (s1[i] < s2[i]):
            return False
    if (len(s1) > len(s2)):
        return True
    else:
        return False


def ans():
    s = input()
    suffixs = []
    dic = {}
    for i in range(len(s)):
        suffixs.append(s[i:])
        dic[s[i:]] = i
    bubbleSort(suffixs)
    res = []
    for i in range(len(s)):
        res.append(dic[suffixs[i]]+1)
    for i in range(len(res)-1):
        print(res[i],"",end="")
    print(res[len(res)-1])


if __name__ == '__main__':
    ans()
