s = input()
res = 0
for back in range(1, len(s)+1, 1):
    for start in range(0, back-2, 1):
        for l in range(1 ,back - start ,1):
            if start+l > back-l:
                if s[start:start+l] == s[back-l:back]:
                    res += l
    print(res)