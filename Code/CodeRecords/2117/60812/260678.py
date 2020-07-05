n = int(input())
l = ['1' for i in range(n)]
for i in range(2, n+1):
    for j in range(i-1, n, i):
        l[j] = str(1-int(l[j]))
print(''.join(l).count('1'))