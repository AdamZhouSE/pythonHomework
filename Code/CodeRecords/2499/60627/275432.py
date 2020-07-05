#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<cmath>
using namespace std;

const int RANGE=1000005;

int n,c[RANGE*2+1005],tot;
pair<int,pair<int,int> > a[100005];
bool vis[100005];

void ins(int x,int y)
{
    x+=RANGE+1;x=max(x,1);x=min(x,n);
    while (x<=n) c[x]+=y,x+=x&(-x);
}

int query(int x)
{
    int ans=0;x+=RANGE+1;x=max(x,1);x=min(x,n);
    while (x) ans+=c[x],x-=x&(-x);
    return ans;
}

int main()
{
    n=RANGE*2+1000;
    int T;
    scanf("%d",&T);
    while (T--)
    {
        char ch[10];
        scanf("%s",ch);
        if (ch[0]=='A')
        {
            int x,y,z;
            scanf("%d%d%d",&x,&y,&z);
            tot++;a[tot]=make_pair(x,make_pair(y,z));
            if (x==0)
            {
                if (y>z) ins(-RANGE,1);
                continue;
            }
            if ((z-y)%x==0)
                if (x<0) ins(-RANGE,1),ins((z-y)/x,-1);
                else ins((z-y)/x+1,1);
            else
                if (x<0) ins(-RANGE,1),ins((int)floor((double)(z-y)/x)+1,-1);
                else ins((int)floor((double)(z-y)/x)+1,1);
        }
        else if (ch[0]=='D')
        {
            int w;
            scanf("%d",&w);
            if (vis[w]) continue;
            vis[w]=1;
            int x=a[w].first,y=a[w].second.first,z=a[w].second.second;
            if (x==0)
            {
                if (y>z) ins(-RANGE,-1);
                continue;
            }
            if ((z-y)%x==0)
                if (x<0) ins(-RANGE,-1),ins((z-y)/x,1);
                else ins((z-y)/x+1,-1);
            else
                if (x<0) ins(-RANGE,-1),ins((int)floor((double)(z-y)/x)+1,1);
                else ins((int)floor((double)(z-y)/x)+1,-1);
        }
        else
        {
            int w;
            scanf("%d",&w);
            printf("%d\n",query(w));
        }
    }
    return 0;
}