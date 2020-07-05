import math
def rotateDirection(pre_face,instr,X,Y,dis):
    dt={}
    if instr=="U":
        if pre_face=="N":
            Y+=dis
        elif pre_face=="S":
            Y-=dis
        elif pre_face=="E":
            X+=dis
        else:
            X-=dis
        return pre_face,X,Y

    elif instr=="D":
        dt={"N":"S", "S":"N", "E":"W", "W":"E"}
        if pre_face=="N":
            Y-=dis
        elif pre_face=="S":
            Y+=dis
        elif pre_face=="E":
            X-=dis
        else:
            X+=dis
    elif instr=="L":
        dt={"N":"W", "S":"E", "E":"N", "W":"S"}
        if pre_face=="N":
            X-=dis
        elif pre_face=="S":
            X+=dis
        elif pre_face=="E":
            Y+=dis
        else:
            Y-=dis
    else:#向右转
        dt={"N":"E", "S":"W", "E":"S", "W":"N"}
        if pre_face == "N":
            X += dis
        elif pre_face == "S":
            X -= dis
        elif pre_face == "E":
            Y -= dis
        else:
            Y += dis
    return dt[pre_face],X,Y


def solution(a,n,x,y):
    instr = [ a[i] for i in range(len(a)) if i%2 == 0 ]
    dis = [ a[i] for i in range(len(a)) if i%2 != 0 ]
    dis = [ int(x) for x in dis ]
    face, x, y = rotateDirection("N", instr[0], 0, 0, dis[0] )
    for k in range(1,n):
        face, x, y = rotateDirection( face, instr[k], x, y, dis[k] )
    final_dis = int( math.sqrt( x**2 + y**2 ) )
    return face, final_dis


if __name__=="__main__":
    n=int(input())
    for _ in range(n):
        n=int(input())
        a=input().split()
        face,final_dis=solution(a,n,0,0)
        print(final_dis,end=" ")
        print(face)
