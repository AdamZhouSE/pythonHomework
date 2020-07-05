yuan = ["a", "o", "e", "i", "u", "v"]
n = int(input())
for i in range(n):
    s = input()
    m = []
    end = 1 << len(s)
    for j in range(end):
        subset = ''
        for k in range(len(s)):
            if (j >> k) % 2 == 1:
                subset += s[k]
        m.append(subset)
    m = sorted(m)
    x = False
    for k in m:
        if k != '':
            if k[0] in yuan and k[len(k) - 1] not in yuan:
                if k != m[len(m) - 1]:
                    print(k, end='')
                else:
                    print(k, end='\n')
                x = True
    if x == False:
        print("-1")