input()
num = set([int(x) for x in input().split()])
num.discard(0)
print(len(num))
