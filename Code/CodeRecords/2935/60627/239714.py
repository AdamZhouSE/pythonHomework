# 6
inp = input()
n = len(inp)
t = 0
for i in range(n):
    for j in range(i,n):
        for k in range(j,n):
            if inp[i] == 'Q' and inp[j] == 'A' and inp[k] == 'Q':
                t += 1
print(t,end = '')