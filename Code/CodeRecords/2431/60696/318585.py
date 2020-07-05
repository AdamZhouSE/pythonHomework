#include <iostream>
#include <string>
#include <cstring>
#include <algorithm>
#include <cmath>
using namespace std;
int t;
struct newt {
    int from,to;
    double jl;
}edge[250005];
struct newtt{
    double x,y;
}dian[505];
int father[505];
int s,n;
bool cmp(newt a,newt b)
{
    return a.jl<b.jl;
}
bool cmp1(newt a,newt b)
{
    return a.jl>b.jl;
}
double js(newtt a,newtt b)
{
    return sqrt((a.x-b.x)*(a.x-b.x)+(a.y-b.y)*(a.y-b.y));
}
void init()
{
    for(int i=1;i<=n;i++)
    father[i]=i;
}
int fi(int x)
{
    if(x==father[x])return x;
    return father[x]=fi(father[x]);
}
bool same(int x,int y)
{
    if(fi(x)==fi(y))return 1;
    return 0;
}
void Union(int x,int y)
{
    int u=fi(x),v=fi(y);
    if(u==v)return ;
    father[u]=v;
}
void check()
{
    double ans=0;
    s=n-s;
    for(int i=1;i<t,s>0;i++)
    {
        if(!same(edge[i].from,edge[i].to))
        {
            ans=max(edge[i].jl,ans);
            Union(edge[i].from,edge[i].to);
            s--;
        }
        
    }
    printf("%.2lf\n",ans);
    
}
int main()
{
    cin>>s>>n;
    for(int i=1;i<=n;i++)
    cin>>dian[i].x>>dian[i].y;
 	t=1;
    for(int i=1;i<=n;i++)
    {
        for(int j=i+1;j<=n;j++)
        {
            edge[t].from=i;
            edge[t].to=j;
            edge[t++].jl=js(dian[i],dian[j]);
        }
    }
    //cout<<js(dian[1],dian[4])<<endl;
    init();
    sort(edge+1,edge+t,cmp);
    check();	
}