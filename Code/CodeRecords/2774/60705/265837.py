test = int(input())
for i in range(0, test):
    [n, k] = list(map(int, input().split(" ")))
    price = list(map(int, input().split(" ")))
    price.sort()
    for j in range(0, n+1):
        if sum(price[0:j]) > k:
            break
    print(j-1)