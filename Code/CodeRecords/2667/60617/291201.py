def MidoriAndChocolate():
    row = input().split(" ")
    i = int(row[0])
    N = int(row[1])
    shop = 0
    for j in range(0, N):
        shop += 2 ** j
    print(shop - i + 1)
    if shop-i+1==28:
        print(row)
if __name__ == '__main__':
    T = int(input())
    for i in range(0, T):
        MidoriAndChocolate()