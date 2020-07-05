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
    result = []
    x = False
    for k in m:
        if k != '':
            if k[0] in yuan and k[len(k) - 1] not in yuan and k not in result:
                result.append(k)
                x = True
    if x == False:
        print("-1")
    for j in result:
        if j != result[len(result) - 1]:
            print(j,end=' ')
        else:
            print(j)