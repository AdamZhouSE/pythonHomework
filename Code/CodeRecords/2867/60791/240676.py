a=[]
try:
    while True:
        inp = input().split()
        a.append(inp)
except EOFError:
    pass
mm = 0
nn = 1
for m in range(len(a)):
    for n in range(len(a)):
        if(a[m][n] == '1'):
            mm = m
            nn = n
print(abs(2-mm)+abs(2-nn))
        