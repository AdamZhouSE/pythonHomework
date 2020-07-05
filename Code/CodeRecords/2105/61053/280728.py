def recArea(x1,y1,x2,y2,x3,y3,x4,y4):
    overlap = 0
    if (x2 <= x3 or x4 <= x1) and (y2 <= y3 or y4 <= y1):
        overlap = 0
    else:
        lens = min(x2, x4) - max(x1, x3)
        wide = min(y2, y4) - max(y1, y3)
        overlap = lens * wide
    return (x2-x1)*(y2-y1) + (x4-x3)*(y4-y3) - overlap

if __name__ == "__main__":
    coors = list(map(int,input().split(",")))
    ans = recArea(coors[0],coors[1],coors[2],coors[3],coors[4],coors[5],coors[6],coors[7])
    print(ans)