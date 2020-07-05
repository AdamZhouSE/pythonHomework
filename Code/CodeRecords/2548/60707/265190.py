num = int(input())
while num > 0:
    str1 = input()
    k = int(input())
    m = 0
    length = len(str1)
    for i in range(length):
        p = 0
        a = [0] * 26
        for j in range(i, length):
            a[ord(str1[j]) - ord('a')] =1
            p = 0
            for t in range(26):
                if a[t]:
                    p += 1
            if p <= k:
                m = max(m, j - i + 1)
    print(str(m))
    num -= 1