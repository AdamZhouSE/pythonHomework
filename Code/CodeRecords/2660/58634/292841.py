n = int(input())
article = []
orders = []
for i in range(n):
    order,x = input().split(" ")
    if order == "T":
        article.append(x)
        orders.append((order, x))
    elif order == "Q":
        print(article[int(x)-1])
        # 不算修改操作 不管
    else:
        for k in range(int(x)):
            article.pop()


