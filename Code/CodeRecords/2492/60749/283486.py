#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
int n,m,nx,ny;
struct field
{
    int x,y;
}p[510];
int rx[510],ry[510],s[510];
bool cmp1(field a,field b)
{
    return a.x<b.x;
}
bool cmp2(field a,field b)
{
    return a.y<b.y;
}
bool solve(int ml)
{
    int i,a,b,c,d,sc,sd;
    a=b=0;
    memset(s,0,sizeof(s));
    while(b<n&&rx[p[b+1].x]-rx[1]+1<=ml)  s[p[++b].y]++;
    for(;b<=n;s[p[++b].y]++)
    {
        while(rx[p[b].x]-rx[p[a+1].x]+1>ml)  s[p[++a].y]--;
        c=d=sc=sd=0;
        while(d<ny&&ry[d+1]-ry[1]+1<=ml)  sd+=s[++d];
        for(;d<=ny;sd+=s[++d])
        {
            while(ry[d]-ry[c+1]+1>ml)    sc+=s[++c];
            if(sd-sc>=m) return true;
        }
    }
    return false;
}
int main()
{
    scanf("%d%d",&m,&n);
    int i;
    rx[0]=ry[0]=-1;
    for(i=1;i<=n;i++)    scanf("%d%d",&p[i].x,&p[i].y);
    sort(p+1,p+n+1,cmp2);
    for(i=1;i<=n;i++)
    {
        if(p[i].y>ry[ny])    ry[++ny]=p[i].y;
        p[i].y=ny;
    }
    sort(p+1,p+n+1,cmp1);
    for(i=1;i<=n;i++)
    {
        if(p[i].x>rx[nx])    rx[++nx]=p[i].x;
        p[i].x=nx;
    }
    int l=1,r=max(rx[nx],ry[ny]),mid;
    while(l<r)
    {
        mid=l+r>>1;
        if(solve(mid))  r=mid;
        else    l=mid+1;
    }
    printf("%d",r);
    printf("\n")
    return 0;
}