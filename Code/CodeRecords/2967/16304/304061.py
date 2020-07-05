def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    length = len(strs)
    if length == 0:
        return ''
    elif length == 1:
        return strs[0]
    else:
        result = ''
        strs_sorted = sorted(strs, key=lambda x: len(x))
        # 最短字符串
        shortest = strs_sorted[0]
        k = 0
        Flag = True
        for s in strs_sorted[1:]:
            for i in range(0, len(shortest)):
                if shortest[:i + 1] in s:
                    k = i
                else:
                    k = i
                    Flag = False
                    break
        # print(k)
        if Flag == True and k >= 0:
            return shortest[:k + 1]
        else:
            return shortest[:k]

num = input()
strs = []
for i in range(int(num)):
    strs.append(input())

print(len(longestCommonPrefix(strs)))