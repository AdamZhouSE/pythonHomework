#投影到x,y轴变成2组线段重叠
T=int(input())
for i in range(0,T):
    square1=list(map(int,input().split()))
    square2=list(map(int,input().split()))
    s1_x1=square1[0]
    s1_y1=square1[1]
    s1_x2=square1[2]
    s1_y2=square1[3]
    s2_x1 = square2[0]
    s2_y1 = square2[1]
    s2_x2 = square2[2]
    s2_y2 = square2[3]
    if max(s1_x1,s2_x1)<=min(s1_x2,s2_x2) and max(s1_y2,s2_y2)<=min(s1_y1,s2_y1):
        print(1)
    else:
        print(0)