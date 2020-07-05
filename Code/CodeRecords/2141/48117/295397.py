def intToBinary(n : int) -> str:
    ans = ''
    while n > 0:
        ans += str(n % 2)
        n //= 2
    return ans[::-1]




questNum = int(input())

for quest in range(questNum):
    n = int(input())

    for i in range(1, n + 1):
        if i != n:
            print(intToBinary(i), end=' ')
        else:
            print(intToBinary(n), end=' ')
            print()