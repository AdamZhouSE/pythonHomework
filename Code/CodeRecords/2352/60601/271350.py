maxn = 2010
n,m,q = 0,0,0
a = [[0 for i in range(maxn)] for j in range(maxn)]
b = [[0 for i in range(maxn)] for j in range(maxn)]
c = [[0 for i in range(maxn)] for j in range(maxn)]

def calc(a:list,x1:int,y1:int,x2:int,y2:int):
    if x1>x2 or y1>y2:
        return 0
    return a[x2][y2] - a[x1 - 1][y2] - a[x2][y1 - 1] + a[x1 - 1][y1 - 1]

line = input().split(' ')
n = int(line[0])
m = int(line[1])
q = int(line[2])
for i in range(1,n+1):
    s = '0'+input()
    for j in range(1,m+1):
        a[i][j] = ord(s[j])-ord('0')
for i in range(2,n+1):
    for j in range(1,m+1):
        b[i][j] = a[i][j] & a[i-1][j]
for i in range(1,n+1):
    for j in range(2,m+1):
        c[i][j] = a[i][j] & a[i][j-1]
for i in range(1,n+1):
    for j in range(1,m+1):
        a[i][j] = a[i][j] + a[i - 1][j] + a[i][j - 1] - a[i - 1][j - 1]
        b[i][j] = b[i][j] + b[i - 1][j] + b[i][j - 1] - b[i - 1][j - 1]
        c[i][j] = c[i][j] + c[i - 1][j] + c[i][j - 1] - c[i - 1][j - 1]
while q:
    line = input().split(' ')
    x1 = int(line[0])
    y1 = int(line[1])
    x2 = int(line[2])
    y2 = int(line[3])
    print(calc(a,x1,y1,x2,y2)-calc(b,x1+1,y1,x2,y2)-calc(c,x1,y1+1,x2,y2))
    q = q - 1