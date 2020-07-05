def allCellsDistOrder(R, C, r0, c0):
    dist_list = [[] for i in range(200)]
    for i in range(R):
        for j in range(C):
            distinct = abs(r0 - i) + abs(c0 - j)
            dist_list[distinct].append([i, j])
    result = []
    for i in dist_list:
        if i:
            result.extend(i)
        else:
            break
    return result


R = int(input())
C = int(input())
r0 = int(input())
c0 = int(input())
res = allCellsDistOrder(R,C,r0,c0)
print(res)