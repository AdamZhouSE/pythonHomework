#include <bits/stdc++.h>
#include <cstring>
#define ll long long
#define INF 0x3f3f3f3f
using namespace std;
const double eps = 1e-8;
const double PI = acos(-1.0);
struct Point
{
    double x,y;
    Point() {}
    Point(double _x,double _y)
    {
        x = _x;
        y = _y;
    }
    Point operator -(const Point &b)const
    {
        return Point(x - b.x,y - b.y);
    }
//叉积
    double operator ^(const Point &b)const
    {
        return x*b.y - y*b.x;
    }
//点积
    double operator *(const Point &b)const
    {
        return x*b.x + y*b.y;
    }
//绕原点旋转角度B（弧度值），后x,y的变化
    void transXY(double B)
    {
        double tx = x,ty = y;
        x = tx*cos(B) - ty*sin(B);
        y = tx*sin(B) + ty*cos(B);
    }
};
Point p1,p2,p3,p4;
double GetCross(Point& p1,Point& p2,Point& p)
{
    return (p2-p1)^(p-p1);
}
bool pd(Point p)
{
    return GetCross(p1,p2,p) * GetCross(p3,p4,p) >= 0 && GetCross(p2,p3,p) * GetCross(p4,p1,p) >= 0;
}
int main()
{
    int n,d;
    cin>>n>>d;
    p1=Point(0,d);
    p2=Point(d,0);
    p3=Point(n,n-d);
    p4=Point(n-d,n);
    int T;
    cin>>T;
    while(T--)
    {
        int x,y;
        cin>>x>>y;
        if(pd(Point(x,y)))
            puts("YES");
        else puts("NO");
    }
    return 0;
}