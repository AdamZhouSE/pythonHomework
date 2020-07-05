n = int(input())
length = [int(x) for x in input().split()]
length.sort()
print(pow(sum(length[0: int(n / 2)]), 2) + pow(sum(length[int(n / 2): n]), 2))
