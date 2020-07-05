def area(x1,y1,x2,y2):
    height = y2 - y1
    width = x2 - x1
    return height*width

position = input().split(',')
pos = [ int(i) for i in position ]

area1 = area(pos[0],pos[1],pos[2],pos[3])
area2 = area(pos[4],pos[5],pos[6],pos[7])
area1_2 = area(pos[4],pos[1],pos[2],pos[7])

print(area1+area2-area1_2)