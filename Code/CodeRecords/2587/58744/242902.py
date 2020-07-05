points = list(eval(input().split(' = ')[1]))

def minTimeToVisitAllPoints() -> int:
    time = 0
    i = 0
    
    for j in range(len(points) - 1):
        if i + 1 >= len(points):
            break
        
        src = points[i]
        dest = points[i + 1]
        i += 1
        while not (src[0] == dest[0] and src[1] == dest[1]):
            if src[0] == dest[0]:
                time += abs(dest[1] - src[1])
                break
            elif src[1] == dest[1]:
                time += abs(dest[0] - src[0])
                break
            else:
                time += 1
                if src[0] < dest[0]:
                    src[0] += 1
                    if src[1] < dest[1]:
                        src[1] += 1
                    else:
                        src[1] -= 1
                else:
                    src[0] -= 1
                    if src[1] < dest[1]:
                        src[1] += 1
                    else:
                        src[1] -= 1
    
    return time

print(minTimeToVisitAllPoints())
