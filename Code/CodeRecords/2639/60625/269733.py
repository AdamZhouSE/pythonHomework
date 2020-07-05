def characterReplacement(s, k):
    n = len(s)
    count = [0] * 26
    l, r, cmax, res = 0, 0, 0, 0
    while r < n:
        count[ord(s[r]) - ord('A')] += 1
        cmax = max(cmax, count[ord(s[r]) - ord('A')])
        while r - l + 1 - cmax > k:
            count[ord(s[l]) - ord('A')] -= 1
            l += 1
        res = max(res, r - l + 1)
        r += 1
    return res


s=input()
k=int(input())
print(characterReplacement(s,k))