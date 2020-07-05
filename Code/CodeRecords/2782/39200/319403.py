n = int(input())
ai = []
for i in range(n):
    ai.append(int(input()))
res = ai[0]
for i in range(1, len(ai)):
    b = [abs(ai[x] - ai[i]) for x in range(i)]
    res += min(b)
print(res)
