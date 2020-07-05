from collections import Counter

count = int(input())
for _ in range(count):
    case = [list(map(int, input().split(" "))), list(map(int, input().split(" ")))]
    x1, y1, x2, y2 = case[0][0], case[0][1], case[0][2], case[0][3]
    x3, y3, x4, y4 = case[1][0], case[1][1], case[1][2], case[1][3]
    # x1,y1,x2,y2=10,0,0,10
    # x3,y3,x4,y4=0,0,10,10
    if x1 == x2:
        if x3 < x1 < x4 or (x3 == x1 and min(y1, y2) <= y3 <= max(y1, y2)) or (
                x4 == x1 and min(y1, y2) <= y4 <= max(y1, y2)):
            print(1)
        else:
            print(0)
    elif x3 == x4:
        if x1 < x3 < x2 or (x3 == x1 and min(y3, y4) <= y1 <= max(y3, y4)) or (
                x4 == x2 and min(y3, y4) <= y2 <= max(y3, y4)):
            print(1)
        else:
            print(0)
    else:
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        if x3 > x4:
            x3, x4 = x4, x3
            y3, y4 = y4, y3
        begin = x3 if x1 < x3 else x1
        end = x4 if x4 < x2 else x2
        flag = 0
        sub=((y2 - y1) * (begin - x1) / (x2 - x1) + y1)-((y4 - y3) * (begin - x3) / (x4 - x3) + y3)
        for i in range(begin, end + 1):
            r1 = (y2 - y1) * (i - x1) / (x2 - x1) + y1
            r2 = (y4 - y3) * (i - x3) / (x4 - x3) + y3
            if r1 == r2:
                flag = 1
                break
        for i in range(begin+1,end+1):
            r1 = (y2 - y1) * (i - x1) / (x2 - x1) + y1
            r2 = (y4 - y3) * (i - x3) / (x4 - x3) + y3
            c=r1-r2
            if c*sub<0:
                flag=1
            sub=c
        if flag == 0:
            print(0)
        else:
            print(1)

