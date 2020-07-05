S = list(input())
T = list(input())
same = []
diff = []


for s in S:
    if s in T:
        same.append(s)
for t in T :
    if t not in same:
        diff.append(t)

result1 = ''.join(same)
result2 = ''.join(diff)
result = result1 +result2
print(result)