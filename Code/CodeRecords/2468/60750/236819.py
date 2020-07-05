def solve():
    num = int(input())
    res = []
    while num > 0:
        num = num - 1
        temp = []
        num_temp = int(input())
        data = list(map(lambda x: int(x),list(input().split(' '))))
        for i in range(0,num_temp):
            product = 1
            for j in range(0,num_temp):
                if j != i:
                    product = product * data[j]
            temp.append(product)
        res.append(temp)
    return res

res = solve()
for i in range(0,len(res)):
    for j in range(0,len(res[i])):
        print(res[i][j],end=' ')
    print()
