'''
向量a×向量b（×为向量叉乘）行列式的值（第一行为a两坐标，第二行为b两坐标）
若结果小于0，表示向量b在向量a的顺时针方向；
若结果大于0，表示向量b在向量a的逆时针方向；
若等于0，表示向量a与向量b平行。

假设有两条线段AB，CD，若AB，CD相交，我们可以确定：
1.线段AB与CD所在的直线相交，即点A和点B分别在直线CD的两边；
2.线段CD与AB所在的直线相交，即点C和点D分别在直线AB的两边；

线段AB与线段CD相交，于是我们可以得到两个向量AC，AD，C和D分别在AB的两边或在边上
向量AC在向量AB的逆势针方向，AB×AC > =0；向量AD在向量AB的顺势针方向，AB×AD < =0，两叉乘结果异号或其中一个叉乘不为0另一个叉乘为0。
A，B在C，D两边同理

判断是否共线：
首先，我们给没条线段的两个端点排序，大小判断方法如下：横坐标大的点更大，横坐标相同，纵坐标大的点更大。
排好序后，每条线段中，小的点当起点，大的当终点。
我们可以在两条线段中各取一点，用这两点组成的向量与其中一条线段进行叉乘，结果若为0，就表示两线段共线

若一条线段AB与另一条线段CD共线，且线段AB的起点小于等于线段CD的起点，但线段AB的终点（注意是终点）大于等于线段CD的起点（注意是起点），
或者交换一下顺序，CD的终点大于AB的起点......只要满足其中一个，就表示有重合部分。
'''
t=int(input())
def mult(ax,ay,bx,by,cx,cy):
    return (ax-cx)*(by-cy)-(bx-cx)*(ay-cy)
def interact(ax,ay,bx,by,cx,cy,dx,dy):
    if (max(ax, bx) < min(cx, dx)):
        return 0;
    if (max(ay, by) < min(cy, dy)):
            return 0;
    if (max(cx, dx) < min(ax, bx)):
        return 0;
    if (max(cy, dy) < min(ay, by)):
        return 0;
    if (mult(cx,cy,bx,by,ax,ay) * mult(bx,by,dx,dy,ax,ay) < 0):
        return 0;
    if (mult(ax,ay,dx,dy,cx,cy) * mult(dx,dy,bx,by,cx,cy) < 0):
        return 0;
    return 1;
for i in range(t):
    o1=eval('['+input().replace(' ',',')+']')
    o2=eval('['+input().replace(' ',',')+']')
    ax=o1[0]
    ay=o1[1]
    bx=o1[2]
    by=o1[3]
    cx=o2[0]
    cy=o2[1]
    dx=o2[2]
    dy=o2[3]
    print(interact(ax,ay,bx,by,cx,cy,dx,dy))