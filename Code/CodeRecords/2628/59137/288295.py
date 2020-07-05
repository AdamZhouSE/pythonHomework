def s25():

    import math

    def solve(x, y, x1, y1, x2, y2, x3, y3):
        d12 = (x1 - x2)**2 + (y1 - y2)**2
        d13 = (x1 - x3)**2 + (y1 - y3)**2
        d23 = (x2 - x3)**2 + (y2 - y3)**2
        d1 = (x - x1)**2 + (y - y1)**2
        d2 = (x - x2)**2 + (y - y2)**2
        d3 = (x - x3)**2 + (y - y3)**2

        if d1 == 0 or d2 == 0 or d3 == 0:
            return False

        cos12 = (d1 + d2 - d12) / (2 * math.sqrt(d1) * math.sqrt(d2))
        cos13 = (d1 + d3 - d13) / (2 * math.sqrt(d1) * math.sqrt(d3))
        cos23 = (d2 + d3 - d23) / (2 * math.sqrt(d2) * math.sqrt(d3))

        if cos12 == -1 or cos13 == -1 or cos23 == -1:
            return False
        angle = math.acos(cos12) + math.acos(cos13) + math.acos(cos23)
        if angle < 2 * math.pi - 0.0000000001:
            return False
        return True

    num = int(input())
    for x in range(num):
        triangle1 = input().split()
        triangle2 = input().split()
        triangle3 = input().split()

        x1 = int(triangle1[0])
        x2 = int(triangle2[0])
        x3 = int(triangle3[0])
        y1 = int(triangle1[1])
        y2 = int(triangle2[1])
        y3 = int(triangle3[1])

        x_max = max(max(x1, x2), x3)
        y_max = max(max(y1, y2), y3)
        x_min = min(min(x1, x2), x3)
        y_min = min(min(y1, y2), y3)

        count = 0
        for x in range(x_min, x_max+1):
            for y in range(y_min, y_max+1):
                if solve(x, y, x1, y1, x2, y2, x3, y3):
                    count += 1
        print(count)
        
        
s25()