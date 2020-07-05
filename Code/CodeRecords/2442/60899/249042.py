a = "".join(input().split("["))
a = "".join(a.split("]"))
a = list(map(int,a.split(",")))
a.sort()
if len(a)<2:
    print(0)
else:
    maxsub = 0
    for i in range(len(a)-1):
        maxsub = max(a[i+1]-a[i],maxsub)
    print(maxsub)