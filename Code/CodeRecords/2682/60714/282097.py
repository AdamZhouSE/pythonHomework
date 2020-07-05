T = int(input())
for i in range(0, T):
    n, left, right = [int(x) for x in input().split()]
    temp = bin(n)[2:]
    temp = temp[: len(temp) - right] + "1" * (right - left + 1) + temp[len(temp) - left + 1:]
    print(int(temp, 2))
