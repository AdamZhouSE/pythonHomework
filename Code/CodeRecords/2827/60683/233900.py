n = eval(input())
src = [int(x) for x in input().split()]
src.sort()
print(' '.join([str(x) for x in src]))