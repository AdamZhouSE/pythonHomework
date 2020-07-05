# 9
inp = input()
n = len(inp)
print(inp)
for i in range(n):
    for j in range(n):
        s = inp[i:j]
        if inp[j:].find(s) == 1:
            print('111')
            