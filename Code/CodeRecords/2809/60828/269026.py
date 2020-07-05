def h26():
    n = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    x = 0
    y = 0
    for i in range(int(n / 2)):
        x += arr[i]
        y += arr[n - 1 - i]
    if(n%2!=0):
        y += arr[int(n/2)]
    res = x*x + y*y
    print(res)


if __name__ == '__main__':
    h26()