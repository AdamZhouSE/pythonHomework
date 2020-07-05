def h32():
    n = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    coins = 0
    for i in range(1,n):
        if(arr[i] <= arr[i-1]):
            d = arr[i-1] + 1 - arr[i]
            arr[i] += d
            coins += d
    print(coins)


if __name__ == '__main__':
    h32()
