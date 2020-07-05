def func(n):  # 用于判定某int数的二进制表示中是否有连续的1
    return (n & n<<1) > 0


tests = int(input())
for i in range(tests):
    n = int(input())
    cnt = 0
    for j in range(2**n):
        if not func(j):
            cnt += 1
    print(cnt)
