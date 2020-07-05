def isPrime(n):
    if n == 1:
        return False
    m = 2
    while m <= n/2:
        if n % m == 0:
            return False
        m += 1
    return True


tests = int(input())
nums = []
for i in range(tests):
    nums.append(input())
for i in range(tests):
    Nums = nums[i].split(' ')
    answer = []
    for j in range(int(Nums[0]), int(Nums[1])+1):
        if isPrime(j):
            answer.append(j)
    for k in range(len(answer)):
        if k != len(answer)-1:  # 这道题要求输出结尾无空格（口区）
            print(str(answer[k]), end=' ')
        else:
            print(answer[k], end='')
    print()