a=[int(x) for x in input().lstrip("[").rstrip("]").split(",")]

a.sort()

print(a[len(a)-1])