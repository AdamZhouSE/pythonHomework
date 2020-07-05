def numOfSpell(s):
    # print(s)
    t = []
    for i in range(len(s)):
        for j in range(len(s)-i):
            # print(s[j:j+i+1])
            # a = sorted(list(s[j:j+i+1]))
            a = list(s[j:j+i+1])
            # print(a)
            if not a in t:
                t.append(a)
    # print(t)
    return len(t)

n = int(input())
s = ''.join((''+input()).split(' '))
# print(s)
t = []
for i in range(n):
    for j in range(n - i+1):
        a = list(s[j:j+i+1])
        if not a in t:
            t.append(a)
            print(numOfSpell(s[j:j+i+1]))