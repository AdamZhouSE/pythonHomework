#处理输入
number = int(input())
test = []
for i in range(number):
    n,k = input().split(' ')
    test.append([int(n),int(k)])

res = []
for x in test:
    page = 1
    for i in range(1,x[0]):
        page*=x[1]
    res.append(page)
for i in range(len(res)):
    print(res[i])