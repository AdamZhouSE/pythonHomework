data = list(map(int, input().split(',')))
if sorted(data) == list(range(min(data), max(data)+1)):
    print([0,0])
else:
    pass
