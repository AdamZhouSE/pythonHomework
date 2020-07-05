n = int(input())
shose = input().split()
res = 0
count = 0
elements = []
for i in range(n*2):
    if shose[i] not in elements:
        elements.append(shose[i])
        count += 1
        res = max(count, res)
    elif shose[i] in elements:
        count -= 1
print(res)