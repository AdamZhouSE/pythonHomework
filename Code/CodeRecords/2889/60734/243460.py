n = int(input())
lst = input().split(' ')
lst = list(map(int,lst))

print("{:.6f}".format(sum(lst)/n))