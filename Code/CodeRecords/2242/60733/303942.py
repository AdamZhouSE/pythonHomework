def isRectangleOverlap(rec1, rec2):
    def intersect(p_left, p_right, q_left, q_right):
        return min(p_right, q_right) > max(p_left, q_left)

    return (intersect(rec1[0], rec1[2], rec2[0], rec2[2]) and
            intersect(rec1[1], rec1[3], rec2[1], rec2[3]))


A = list(map(int, input().split(",")))
B = list(map(int, input().split(",")))
print(isRectangleOverlap(A, B))