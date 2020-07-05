#include <cstdio>
#include <map>
#define ll long long
const int N=2e5+10;
std::map <int,int> ch[N];
int par[N],len[N],las=1,tot=1,n;
ll ans=0;
void extend(int c)
{
    int now=++tot,p=las;
    len[now]=len[p]+1;
    while(p&&!ch[p][c]) ch[p][c]=now,p=par[p];
    if(!p) par[now]=1;
    else
    {
        int x=ch[p][c];
        if(len[x]==len[p]+1) par[now]=x;
        else
        {
            int y=++tot;
            len[y]=len[p]+1,par[y]=par[x],ch[y]=ch[x];
            while(p&&ch[p][c]==x) ch[p][c]=y,p=par[p];
            par[now]=par[x]=y;
        }
    }
    ans=ans+len[now]-len[par[now]];
    las=now;
}
int main()
{
    scanf("%d",&n);
    for(int c,i=1;i<=n;i++)
    {
        scanf("%d",&c);
        extend(c);
        printf("%lld\n",ans);
    }
    return 0;
}