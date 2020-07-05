def contain(small, large):
    for i in small:
        if i in large:
            return True
    return False


[n, m] = list(map(int, input().split(" ")))
ci = list(map(int, input().split(" ")))
friends = []
for f in range(0, m):
    friends.append(list(map(int, input().split(" "))))
i = 1
while i < len(friends):
    for j in range(0, i):
        if contain(friends[i], friends[j]):
            friends[j].extend(friends[i])
            friends.pop(i)
            i = 0
    i += 1
for i in range(0, len(friends)):
    friends[i] = set(friends[i])
# 生成了朋友圈，一个圈子里的人只需要花一次最少的黄金

count = 0
for sets in friends:
    temp = []
    for i in sets:
        temp.append(ci[i-1])
        ci[i-1] = 0
    count += min(temp)
for rest in ci:
    count += rest
print(count)
