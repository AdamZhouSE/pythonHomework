def solve(res):
    temp = []
    for i in range(1, len(res)+1):
        for k in range(len(res)-i+1):
            if temp.count(res[k:k+i]) == 0:
                temp.append(res[k:k+i])
    return str(len(temp))


num = int(input())
all = input().split(" ")
res = []
for i in range(num):
    res.append(all[i])
    print(solve(res))