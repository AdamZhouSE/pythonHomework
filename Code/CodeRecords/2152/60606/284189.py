n = int(input())
orzFang = input().split(" ")
path = input().split(" ")
orzFang = [int(x) for x in orzFang]
path = [int(x) for x in path]
for i in range(n):
    sum = orzFang[i]
    next = path[i]-1
    temp = set()
    temp.add(i)
    size = 0
    last = 0
    while len(temp) != size:
        temp.add(next)
        sum += orzFang[next]
        last = orzFang[next]
        next = path[next]-1
        size += 1
    print(sum-last)
