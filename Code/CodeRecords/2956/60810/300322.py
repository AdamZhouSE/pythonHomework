def mul(f, mat):
    res = []
    for i in range(26):
        temp = 0
        for j in range(26):
            temp += f[j] * mat[j][i]
        res.append(temp)
    return res

def cal(mat, inp, f):
    if (inp == 1): return 26
    for i in range(inp - 1):
        f = mul(f, mat)
    res = 0
    for i in range(26):
        res += f[i]
    return res

inp = int(input())
str = input()
f = []
mat = [[1 for i in range(26)] for i in range(26)]
for i in range(26):
    f.append(1)
for j in range(len(str) - 1):
    mat[ord(str[j]) - 97][ord(str[j + 1]) - 97] = 0
print(cal(mat, inp, f))
