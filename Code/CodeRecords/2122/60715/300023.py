def CanDo( x, y, z):
    from collections import deque
    queue = deque([[0, 0]])
    visited = set([(0, 0)])

    while queue:
        cur_x, cur_y = queue.pop()
        if z in [cur_x, cur_y, cur_x + cur_y]:
            return True
        for item in [
            (x, cur_y), (cur_x, y),
            (0, cur_y), (cur_x, 0),
            (cur_x + cur_y - y, y) if cur_x + cur_y >= y else (0, cur_x + cur_y),
            (x, cur_x + cur_y - x) if cur_x + cur_y >= x else (cur_x + cur_y, 0)]:
            if item not in visited:
                queue.appendleft(item)
                visited.add(item)
    return False
x=int(input())
y=int(input())
z=int(input())
print(CanDo(x,y,z))