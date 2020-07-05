test = int(input())
for i in range(0, test):
    length = int(input())
    arr = list(map(int, input().split(" ")))
    arr.sort()
    arr.reverse()
    price = 0
    for j in range(0, length):
        price += arr[j] * (j+1)
    price -= arr[len(arr)-1]
    print(price)
