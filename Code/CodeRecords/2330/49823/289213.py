def dp(points):
    mem=set()
    result=float('inf')
    for x1,y1 in points:
        for x2,y2 in mem:
            if (x1,y2) in mem and (x2,y1) in mem:
                area=abs(x1-x2)*abs(y1-y2)
                if area and area<result:
                    result=area
        mem.add((x1,y1))
    print(str(result)+'.0000' if result!=float('inf') else '0.0000')
if __name__ == '__main__':
    dp([[int(i) for i in input().split(',')] for _ in range(int(input()))])
