test = int(input())
for i in range(0, test):
    length = int(input())
    arr = list(map(int, input().split(" ")))
    price = 0
    for j in range(0, length-1): # 总共要拼接3次
        arr.sort()
        price += (arr[0] + arr[1])
        a = arr.pop(0)
        b = arr.pop(0)
        arr.append(a+b)
    print(price)

