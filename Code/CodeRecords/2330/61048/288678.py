import math
def numop17():
    num=int(input())
    points = []
    for i in range(num):
        str_in=input().split(',')
        point = list(int(x) for x in str_in)
        points.append(point)
    '''string=str_in[2:len(str_in)-2].split("],[")
    for item in string:
        array=item.split(',')
        point=list(int(x) for x in array)
        points.append(point)'''
    point_4=set()
    res = 10000.0*10000.0
    for x1, y1 in points:
        point_4.add((x1, y1))
        for x2, y2 in points:
            if((x2,y2) not in point_4):
                point_4.add((x2, y2))
                for x3,y3 in points:
                    if((x3,y3)not in point_4):
                        point_4.add((x3,y3))
                        for x4,y4 in points:
                            if((x4,y4)not in point_4):
                                point_4.add((x4,y4))
                                if (x1+x2)/2==(x3+x4)/2 and (y1+y2)/2==(y3+y4)/2:
                                    area = math.sqrt(pow(abs(x1 - x3),2)+pow(abs(y1-y4),2)) * math.sqrt(pow(abs(x1 - x4),2)+pow(abs(y1-y4),2))
                                    if area and area < res:
                                        res = area
                                point_4.remove((x4,y4))
                        point_4.remove((x3, y3))
                point_4.remove((x2, y2))
        point_4.remove((x1, y1))

    if(res==10000.0*10000.0):
        res=0.0000
    print('{:.4f}'.format(res))
    return 0


numop17()