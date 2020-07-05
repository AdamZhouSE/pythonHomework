s = list(input())
for i in range(len(s)):
    s[i] = int(s[i])
num = s[:]
num.sort(reverse = True)
if str(num)==str(s):
    print("".join(str(i) for i in s))
else:
    t = False
    n = 0
    for i in range(len(num)):
        for j in range(i,len(num)):
            if s[j]>s[i]:
                t = True
                n = i
                break
        if t:
            break

    ind_ma = s.index(max(s[i+1:]))
    for i in range(len(s)):
        s[i] = str(s[i])

    s = s[:n] + [s[ind_ma]] + s[n+1:ind_ma] + [s[n]] + s[ind_ma+1:]
    print("".join(str(i) for i in s))