n = int(input())
list1 = []
dict1 = {}
dict2 = {}
for i in range(n):
    list1.append(input().split(" "))
for j in list1:
    if not dict1.get(j[0], None):
        dict1[j[0]] = int(j[1])
    else:
        dict1[j[0]] += int(j[1])
max_scores = max(dict1.values())
for m in list1:
    if not dict2.get(m[0], None):
        dict2[m[0]] = int(m[1])
    else:
        dict2[m[0]] += int(m[1])
    if dict2[m[0]] == max_scores and dict1[m[0]] >= max_scores:
        winner = m[0]
        break
print(winner)