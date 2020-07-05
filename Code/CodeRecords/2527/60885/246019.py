rests = eval(input())
v = int(input())
p = int(input())
d = int(input())
ans = []
for rest in rests:
    if rest[2] >= v and rest[3] <= p and rest[4] <= d:
        ans.append(rest)
ans = sorted(ans, key=lambda x:(x[1],x[0]), reverse=True)
result = []
for rest in ans:
    result.append(rest[0])
print(result)