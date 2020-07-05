def h13():
    n = int(input())
    arr = list(map(int,input().split()))
    a,b = map(int,input().split())
    sum = 0
    for i in range(a,b):
        sum += arr[i-1]
    print(sum)


if __name__ == '__main__':
    h13()