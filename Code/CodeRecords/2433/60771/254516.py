#37
region = list(eval(input()))
while True:
    temp = region[:]
    for i in range(0, len(region)-1):
        sub = []
        if region[i][1] >= region[i + 1][0]:
            sub.append(region[i][0])
            sub.append(region[i + 1][1])
            region.remove(region[i])
            region.remove(region[i])
            region.insert(i,sub)
            break
    if temp == region:
        break
print(region)

