lists = list(map(int, input().split(",")))
target = int(input())

res = []
for i in range(lists.__len__()):
    if lists[i] == target:
        res.append(i)
print(res)