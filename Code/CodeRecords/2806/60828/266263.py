def h23():
    n = int(input())
    amount = []
    price = []
    for i in range(n):
        s = list(map(int,input().split()))
        amount.append(s[0])
        price.append(s[1])
    for i in range(n):
        for j in range(i+1,n):
            if(price[i]<price[j]):
                price[j] = price[i]
    sum = 0
    for i in range(n):
        sum += price[i]*amount[i]
    print(sum)


if __name__ == '__main__':
    h23()