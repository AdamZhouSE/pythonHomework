"""
严格N元树
fi表示深度不超过i的严格N元树数量
fi = f(i-1)^n + 1
f0 = 1
深度恰好为n，即f(n)-f(n-1)
"""
inp = input().split(" ")
n, d = int(inp[0]), int(inp[1])
f = [1]
for i in range(1, d+1):
    f.append(f[i-1]**n + 1)
print(f[d]-f[d-1], end="")
