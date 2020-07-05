a = eval(input())
b = eval(input())
c = [[0]*(len(b)+1) for _ in range(len(a)+1)]


for i in range(len(a)-1, -1, -1):
    for j in range(len(b)-1, -1, -1):
        if a[i] == b[j]:
            c[i][j] = c[i+1][j+1] + 1

print(max(max(c)))