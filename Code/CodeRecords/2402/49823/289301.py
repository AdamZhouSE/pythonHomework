def ds(bookings,n):
    ans = [0] * n
    d = dict()
    for start, end, val in bookings:
        d[start - 1] = d.get(start - 1, 0) + val
        d[end] = d.get(end, 0) - val
    s = 0
    for i in range(n):
        if i in d:
            s += d[i]
        ans[i] = s
    print(ans)
if __name__ == '__main__':
    ds([[int(i) for i in input().split(',')] for _ in range(int(input()))],int(input()))
