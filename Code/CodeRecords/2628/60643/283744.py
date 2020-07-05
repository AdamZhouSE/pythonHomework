def cal_area(x1,y1,x2,y2,x3,y3):
    area=abs(0.5*(x1*y2+x2*y3+x3*y1-x1*y3-x2*y1-x3*y2))
    return area

def gcd(a,b):
    if b>a:#swap
        temp=a
        a=b
        b=temp
    if b==0:
        return a#说明两个点的xy坐标有一个相同，所以这两个点的边上的整点数就是abs(x1-x2)
    elif a%b==0:
        return b
    else:
        return gcd(b,a%b)


if __name__=="__main__":
    n=int(input())
    cnt=0
    while cnt<n:
        x1,y1=input().split()
        x2,y2=input().split()
        x3,y3=input().split()
        x1=int(x1)
        x2=int(x2)
        x3=int(x3)
        y1=int(y1)
        y2=int(y2)
        y3=int(y3)
        area=cal_area(x1,y1,x2,y2,x3,y3)
        L=gcd(abs(x2-x1),abs(y2-y1))+gcd(abs(x3-x2),abs(y3-y2))+gcd(abs(x3-x1),abs(y3-y1))
        inner=int(area-L/2+1)
        print(inner)
        cnt+=1