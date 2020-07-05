def count(subStr, target):
    res = 0
    for i in range(0, len(target) - len(subStr) + 1):
        if target[i] == subStr[0]:
            if target[i:i+len(subStr)] == subStr:
                res += 1
    return res


while True:
    n = int(input())
    strs = []
    freq = {}
    if n == 0:
        break
    for i in range(n):
        strs.append(input())
    target = input()
    for j in strs:
        freq[j] = count(j,target)
    maxF = max(freq.values())
    print(maxF)
    for j in strs:
        if freq[j] == maxF:
            print(j)


