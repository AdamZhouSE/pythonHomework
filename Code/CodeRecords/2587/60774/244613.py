n = int(input())
pointLst = []
for i in range(0,n):
    pointLst.append(list(map(int,input().split(','))))
xcur = pointLst[0][0]
ycur = pointLst[0][1]
step = 0
for item in pointLst:
    step = max(abs(item[0] - xcur),abs(item[1] - ycur)) + step
    xcur = item[0]
    ycur = item[1]
print(step)