count = int(input())
for i in range(count):
    infos=[int(x) for x in input().split()]
    a1 = [int(x) for x in input().split()]
    a2 = [int(x) for x in input().split()]
    for i in a2:
        a1.append(i)
    a1.sort()
    print(a1[infos[2]-1])