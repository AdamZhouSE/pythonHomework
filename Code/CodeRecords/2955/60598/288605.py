s = input()
t = input()
target = int(input())
mat = [[0 for j in range(len(t)+1)] for i in range(len(s)+1)]
mat[0][0] = 0
for i in range(1, len(s)+1):
    mat[i][0] = mat[i-1][0] + target
for j in range(1, len(t)+1):
    mat[0][j] = mat[0][j-1] + target
for i in range(1, len(s)+1):
    for j in range(1, len(t)+1):
        temp1 = mat[i-1][j-1] + abs(ord(s[i-1]) - ord(t[j-1]))
        temp2 = mat[i-1][j] + target
        temp3 = mat[i][j-1] + target
        mat[i][j] = min(temp1, temp2, temp3)
print(mat[len(s)][len(t)],end = "")
