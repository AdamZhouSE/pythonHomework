
n = int(input())
ai = input().split(" ")
for i in range(0, len(ai)):
    ai[i] = int(ai[i])
ai.sort()
k = 1
for i in ai:
    if i < k:
        continue
    else:
        k += 1
print(k-1)