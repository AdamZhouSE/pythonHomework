num = int(input())
total = int(input())
sin = []
ans = 0
for i in range(num):
    sin.append(int(input()))
while total > 0:
    total = total - max(sin)
    sin[list.index(sin, max(sin))] = 0
    ans = ans + 1
print(ans)