def func9():
    m = int(input())
    n = int(input())
    k = int(input())
    low = 1
    high = m*n
    while low < high:
        mid = (low+high)//2
        cnt = 0
        for i in range(1, m+1, 1):
            cnt += min(mid//i, n)
        if k > cnt:
            low = mid+1
        else:
            high = mid
    print(high)
    return
func9()