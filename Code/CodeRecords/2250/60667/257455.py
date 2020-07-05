count = int(input())
points = []
for i in range(count):
    points.append(list(map(int,input().split(','))))
points.sort()  
if len(points) < 3:
    print(len(points))
    quit()
    
lines, p_visited = {}, set() 
for i, (x, y) in enumerate(points): 
    for (_x, _y, j) in p_visited:  
        k, _k, b = None, None, x  
        if _x != x:
            k = (_y-y)/(_x-x)
            _k = (_x-x)/(_y-y) if _y != y else None 
            b = round(y-k*x, 6) 
        lines[(k, _k, b)] = lines.get((k, _k, b), set()) | {(x, y, i), (_x, _y, j)}
    p_visited.add((x, y, i))
print(max(len(x) for x in lines.values()))
