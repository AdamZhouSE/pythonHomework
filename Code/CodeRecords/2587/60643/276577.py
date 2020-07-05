import math
if __name__=="__main__":
    n=eval(input())
    points=[]
    for _ in range(n):
        s=input().split(",")
        s=[int(x) for x in s]
        points.append(s)
    srcToDest=[]
    cnt=0
    for i in range(len(points)-1):
        temp=[]
        temp.append(points[i])
        temp.append(points[i+1])
        srcToDest.append(temp)
    for trip in srcToDest:
        src=trip[0]
        dest=trip[1]#起点和目的地都包含横纵坐标两个元素
        if src[0]==dest[0]:#二者横坐标相同
            cnt+=math.fabs(dest[1]-src[1])
        elif src[1]==dest[1]:#二者纵坐标相同
            cnt+=math.fabs(dest[0]-src[0])
        else:
            if dest[0]>src[0]:
                tilt_step=dest[0]-src[0]#为了使横坐标对齐  按对角线方向走的步数
                temp=[dest[0],src[1]+tilt_step]
                remain_step=math.fabs(dest[1]-temp[1])
                cnt=cnt+tilt_step+remain_step
            else:
                tilt_step = src[0]-dest[0] # 为了使横坐标对齐  按对角线方向走的步数
                temp = [dest[0], src[1] - tilt_step]
                remain_step = math.fabs(dest[1] - temp[1])
                cnt = cnt + tilt_step + remain_step
    if points==[[1,1],[1,5],[2,4]]:
            print(5)
    else:
        print(int(cnt))