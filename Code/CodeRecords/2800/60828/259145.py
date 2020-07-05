def h19():
    s = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    n = s[0]
    d = s[1]
    sum = 0
    for i in range(1,n):
        while(arr[i]<=arr[i-1]):
            arr[i] += d
            sum += 1
    print(sum)

if __name__ == '__main__':
    h19()