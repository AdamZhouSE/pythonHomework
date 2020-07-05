def h20():
    s = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    n = s[0]
    m = s[1]
    num = -1
    l = n
    while(l>0):
        num = (num + 1) % n
        if(not(arr[num]==0)):
            if (arr[num] <= m):
                arr[num] = 0
                l -= 1
            else:
                arr[num] -= m
    print(num+1)


if __name__ == '__main__':
    h20()