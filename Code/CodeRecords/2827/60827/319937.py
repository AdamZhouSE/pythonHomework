n = int(input())
l = [int(x) for x in input().split()]
print(" ".join([str(x) for x in sorted(l)]))