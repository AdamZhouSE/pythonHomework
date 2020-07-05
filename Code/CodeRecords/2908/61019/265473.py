n = eval(input())
src = []
for _ in range(n):
    s = input().strip()
    src.append(s)

total = set()
for s in src:
    fre = {}
    for x in s:
        fre[x] = fre[x] + 1 if x in fre else 1
    fre = [f for f in fre.items()]
    fre.sort()
    fre = str(fre)
    total.add(fre)

# print(total)
print(len(total),end='')
