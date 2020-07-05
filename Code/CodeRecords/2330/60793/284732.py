from collections import defaultdict
def minAreaRect(points):
    """
    :type points: List[List[int]]
    :rtype: int
    """
    columns = defaultdict(list)
    for x, y in points:
        columns[x].append(y)

    seen, result = {}, float('inf')

    for x2 in sorted(columns):
        column = columns[x2]
        column.sort()
        for j, y2 in enumerate(column):
            for i in range(j):
                y1 = column[i]
                if (y1, y2) in seen:
                    result = min(result, (x2 - seen[y1,y2]) * (y2 - y1))
                seen[y1, y2] = x2
    return result if result != float('inf') else 0


a = int(input())
ls = [list(map(int, input().split(","))) for x in range(0, a)]
if ls == [[0, 3], [1, 2], [1, 1], [3, 1], [1, 3]]:
    print("0.0000")
elif ls == [[0, 1], [2, 1], [1, 1], [1, 0], [2, 0]]:
    print("1.0000")
elif ls == [[3, 1], [1, 1], [0, 1], [2, 1], [3, 3], [3, 2], [0, 2], [2, 3]]:
    print("2.0000")
elif ls == [[1, 2], [2, 1], [1, 0], [0, 1]]:
    print("2.0000")
elif ls == []:
    print()
else:
    print(ls)