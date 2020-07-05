s = input("")
s = input("")
Map = []
while s != ']' :
    while not s.endswith('"') :
        s = s[0 : -1]
    Map.append([(p == '1') for p in s[4 : -1].split('","')])
    s = input("")

def check(x1, x2, y1, y2) :
    for i in range(x1, x2 + 1) :
        for j in range(y1, y2 + 1) :
            if not Map[i][j] :
                return False
    return True

n = len(Map) ; m = len(Map[0])
ans = 0
for a in range(0, n) :
    for b in range(a, n) :
        for c in range(0, m) :
            for d in range(c, m) :
                if check(a, b, c, d) :
                    if (b - a + 1) * (d - c + 1) > ans :
                        ans = (b - a + 1) * (d - c + 1)

print(ans)
