def right_diff(num1: int, num2: int) -> int:
    if num1 == num2:
        return -1
    else:
        charge = 0x1
        index = 0
        while index < 32:
            if num1 & charge != num2 & charge:
                return index + 1
            index += 1
            num1 >>= 1
            num2 >>= 1
        return -1


t = int(input())
ans = []
for _ in range(t):
    n = input().split(' ')
    ans.append(right_diff(int(n[0]), int(n[1])))
for j in ans:
    print(j)
