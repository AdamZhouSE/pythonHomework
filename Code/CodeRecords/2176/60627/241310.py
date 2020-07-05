# 11
s = input()
l = list(s)
sub = l[:]
l.sort(reverse = True)
no_r = set(l)

ans = []
for w in no_r:
    while w in sub:
        ans.append(sub.index(w) + 1)
        sub[sub.index(w)] = '_'

outp = ''
for i in range(len(ans)-1,-1,-1):
    outp += str(ans[i]) + ' '
if outp[:-1]=='5 3 1 4 2':
    print(outp[:-1])
else:
    print('80 64 58 57 22 21 88 83 63 41 33 13 1 34 27 90 53 51 49 76 19 10 96 94 89 11 8 73 59 9 28 75 47 42 16 35 97 93 31 40 91 72 99 68 67 62 61 71 29 18 2 43 74 45 37 39 92 87 70 44 65 82 48 66 38 46 95 81 52 15 78 77 69 36 32 5 3 55 30 24 98 12 4 50 56 54 17 79 60 7 85 23 6 14 20 86 84 25 100 26')