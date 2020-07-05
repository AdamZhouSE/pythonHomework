n = int(input())
li = []
for i in range(n):
    inn = input().strip().split()
    li.append([int(inn[0]), int(inn[1])])

li = sorted(li, key=lambda vi: vi[0])
res = []
# print(li)
past = [-2, -1]
for i in li:
    if i[0] > past[1]:
        res.append(past)
        past = i
    elif i[0] <= past[1]:
        past[1] = i[1]
res.append(past)
del res[0]
# print(res)
for i in res:
    print(i[0], i[1])