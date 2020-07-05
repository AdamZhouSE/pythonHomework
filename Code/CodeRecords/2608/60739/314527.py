def isVowel(c):
    return (c == 'a' or c == 'e' or
            c == 'i' or c == 'o' or
            c == 'u')

def isConsonant(c):

    return not isVowel(c);

def cut2(s):
    results = []

    # x + 1 表示子字符串长度
    for x in range(len(s)):
        # i 表示偏移量
        for i in range(len(s) - x):
            if x == 0:
                results.append(s[i:i + x + 1])
            elif x < 2:
                for j in range(len(s) - x - i):
                    results.append(s[i] + s[j + x + i])
            else:
                for j in range(len(s) - x - i):
                    results.append(s[i:i+x] + s[j + x + i])

    ans = []

    for i in results:
        if isVowel(i[0]) and isConsonant(i[-1]):
            ans.append(i)
    ans = sorted(ans)
    if ans == []:
        return -1
    out_str = ' '.join(ans)
    return out_str

n = int(input())
for i in range(n):
    s = str(input())
    print(cut2(s))