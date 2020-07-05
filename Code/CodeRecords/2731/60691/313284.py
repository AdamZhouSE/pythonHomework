n = eval(input())
for i in range(n):
    m = eval(input())
    pro = list(map(int,input().split(' ')))
    l = list(set(pro))
    product = []
    for i in l:
        product.append([i,pro.count(i)])
    sum = 0
    for i in product:
        if i[1]%2!=0:
            i[1] = i[1]-1
        sum = sum + i[1]
    print(sum)
