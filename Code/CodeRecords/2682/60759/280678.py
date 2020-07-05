ts = int(input())
for t in range(ts):
    n, l, r = map(int, input().split(' '))
    b_str = str(bin(n))[2:][::-1]
    ans = ''
    for i in range(len(b_str)):
        ans += '1' if l <= i + 1 <= r else b_str[i]
    print(int(ans[::-1], 2))
