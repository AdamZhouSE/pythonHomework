a = sorted([int(i) for i in input().strip('[|]').split(',')])
if len(a) < 2:
    print(0)
else:
    print(max([a[i+1]-a[i] for i in range(len(a)-1)]))