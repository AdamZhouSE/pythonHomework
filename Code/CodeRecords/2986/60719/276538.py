s1 = input()
s2 = input()
l1 = len(s1)
l2 = len(s2)
d = [[0]*(l1+1)]*(l2+1)
for i in range(1, l1+1):
    d[0][i] = i
for i in range(1, l2):
    d[i][0] = i
for i in range(1, l2+1):
    for j in range(1, l1+1):
        if s1[j-1] == s2[i-1]:
            d[i][j] = min(min(d[i-1][j]+1, d[i][j-1]+1), d[i-1][j-1])
        else:
            d[i][j] = min(min(d[i-1][j]+1, d[i][j-1]+1), d[i-1][j-1]+1)
print(d[l2][l1])