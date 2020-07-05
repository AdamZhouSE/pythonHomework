s = input()
k = int(input())
if k == 1:
    res = s[:]
    for i in range(len(s)):
        s = s[1:] + s[0]
        if s < res:
            res = s
    print(res)
else:
    print(''.join(sorted(list(s))))
