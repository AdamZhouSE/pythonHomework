def find_sub(m, tar):
    result = 0
    for k in range(len(m)):
        if m[k:].find(tar) == 0:
            result += 1
    return result


stringA = input().strip()
stringB = input().strip()
subs = []
for i in range(len(stringA)):
    for j in range(i + 1, len(stringA)+1):
        su = stringA[i:j]
        if su not in subs:
            subs.append(su)
plans = 0
for s in subs:
    plans += find_sub(stringA, s) * find_sub(stringB, s)
print(plans,end="")
