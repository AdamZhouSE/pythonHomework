total = int(input())
res = []
for i in range(0,total):
    ls = sum(list(map(int,input().split(' '))))
    res.append(ls)
res.sort()
print(res[len(res)-1])