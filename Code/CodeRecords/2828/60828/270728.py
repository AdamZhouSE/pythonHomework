def h33():
    n = int(input())
    arr = list(map(int, input().split()))
    e = arr[0]
    for i in range(1,n):
        temp = arr[0]
        for j in range(1, i):
            temp += arr[j] - arr[j - 1]
        e = max(temp,e)
    print(max(0,e))

if __name__ == '__main__':
    h33()