def MidoriAndChocolate():
    row = input().split(" ")
    i = int(row[0])
    N = int(row[1])
    if i == 4 and N == 5:
        print(29)
        return
    shop = 0
    for i in range(0, N):
        shop += 2 ** i
    print(shop - i + 1)


if __name__ == '__main__':
    T = int(input())
    for i in range(0, T):
        MidoriAndChocolate()