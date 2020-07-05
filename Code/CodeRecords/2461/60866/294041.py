def chazhao(a):
    a.sort()
    return a[0]
a=input().split(',')
a=[int(x) for x in a]
print(chazhao(a))