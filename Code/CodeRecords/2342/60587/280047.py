T = int(input())
while T > 0:
    T -= 1
    n, length = input().split(' ')
    n = int(n)
    length = int(length)
    inp = input().split(' ')

    num = n // length
    remain = n % length

    res = ''
    tmp = ''
    for i in range(0, num):
        tmp = inp[i * length + 0:i * length + length]
        tmp.reverse()
        # res += tmp[0]
        for j in range(0, length):
            res = res + tmp[j] + ' '
    tmp = inp[num * length:num * length + remain]
    tmp.reverse()
    # res += tmp[0]
    for i in range(0, len(tmp)):
        res = res + tmp[i] + ' '
    print(res)
