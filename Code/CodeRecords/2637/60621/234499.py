a=[int(x) for x in input().lstrip("[").rstrip("]").split(",")]
b=[x for x in a]
b.sort()

print(a.index(b[len(b)-1]))