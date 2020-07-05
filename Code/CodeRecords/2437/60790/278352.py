#include<cstdio>
#include<algorithm>
#define N 100005
using namespace std;
int n,l,len,m,now,i,ans;
char k;
//x记录这个点的坐标，val记录这个点是线段的头还是线段的尾;
struct P{int x,val;int operator<(const P&t)const{return x<t.x;}}line[N<<1];
main()
{
    scanf("%d%d",&n,&m);
    for(i=0;i<n;++i)
    {
        scanf("%d %c",&len,&k);
        //将线段拆成点;
        if(k=='R')
        {
            line[++l]=(P){now,+1};
            line[++l]=(P){now+=len,-1};
        }
        else
        {
            line[++l]=(P){now,-1};
            line[++l]=(P){now-=len,+1};
        }
    }
    sort(line+1,line+l+1);
    //"扫描..."
    now=line[1].val;
    for(i=2;i<=l;++i)
    {
        if(now>=m) ans+=line[i].x-line[i-1].x;
        now+=line[i].val;
    }
    printf("%d",ans);
}