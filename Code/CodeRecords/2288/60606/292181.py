for i in range(2):
    line = input().split(" ")
    m = int(line[0])
    n = int(line[1])
    height = 0
    left = m
    right = m
    result = 0
    while left < n and right <= n:
        left *= 2
        right = right * 2 + 1
        height += 1
    # 先算满的层数
    result += pow(2, height) - 1
    # 再算剩下的，不会超过当前层数最大
    if n-left+1>0:
        result += min(pow(2, height), n - left + 1)
    if m!=0 and n!=0:
        print(int(result))