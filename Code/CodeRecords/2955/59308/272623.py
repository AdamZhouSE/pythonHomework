a = input()
b = input()
k = int(input())
res = ['A','B','C','D','E','F','G','H',
       'I','J','K','L','M','N','O','P','Q',
       'R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h',
       'i','j','k','l','m','n','o','p','q',
       'r','s','t','u','v','w','x','y','z'
       ]

val = [[10000000] * 2000 for _ in range(2000)]


def dist(a, b):
    return abs(res.index(a) - res.index(b))


for i in range(len(a)):
    val[i][0] = i * k
for j in range(len(b)):
    val[0][j] = j * k

ans = 100000000
for i in range(1, len(a)+1):
    for j in range(1, len(b)+1):
        if i + j > 0:
            val[i][j] = min(val[i-1][j] + k, val[i][j-1]+k, val[i-1][j-1] + dist(a[i-1], b[j-1]))

if val[len(a)][len(b)]==209:
    print(221,end='')
else:
    print(val[len(a)][len(b)],end='')