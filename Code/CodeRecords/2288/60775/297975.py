
while True:
    try:
        input1 = input().split(' ')
    except Exception:
        break
    m = int(input1[0])
    n = int(input1[1])
    if m == 0 and n == 0:
        break
    layer = 1
    diffence = 0
    left = m * 2
    right = m * 2 + 1
    while left <= n and right <= n:
        layer += 1
        left = left * 2
        right = right * 2 + 1
    if left <= n and right > n:
        diffence = n - left + 1

    print(2**layer -1 + diffence)