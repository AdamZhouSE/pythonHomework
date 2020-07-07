#include<stdio.h>
#include<cstring>
#include<iostream>
#include<algorithm>
#include<bitset>
#include<vector>
#include<math.h>
#include<stack>
#include<map>
#include<queue>
#define ls(x) (x<<1)
#define rs(x) ((x<<1)|1)
#define eps 1e-9
using namespace std;
int n;
struct nod
{
    int l,r,ll,rr;
}cw[100005];
int b[300005],cnt,cc[300005];
int sum[800005];
int main()
{
    scanf("%d",&n);
    for(int i=1;i<=n;i++)
    {
        scanf("%d%d",&cw[i].l,&cw[i].r);
        b[++cnt]=cw[i].r;
        cw[i].r--;
        cw[i].ll=b[++cnt]=cw[i].l;
        cw[i].rr=b[++cnt]=cw[i].r;
    }
    sort(b+1,b+1+cnt);
    int tot=unique(b+1,b+1+cnt)-b;
    for(int i=1;i<=n;i++)
    {
        cw[i].l=lower_bound(b+1,b+1+tot,cw[i].l)-b;
        cw[i].r=lower_bound(b+1,b+1+tot,cw[i].r)-b;
        cc[cw[i].l]++;
        cc[cw[i].r+1]--;
    }//离散化
    int cov=0;//总的覆盖长度
    for(int i=1;i<=tot;i++)
    {
        cc[i]+=cc[i-1];
        if(cc[i])cov+=b[i+1]-b[i];
        if(cc[i]==1)sum[i]=b[i+1]-b[i];
        sum[i]+=sum[i-1];
    }
    int ans=0;
    for(int i=1;i<=n;i++)
    {
        ans=max(ans,cov-(sum[cw[i].r]-sum[cw[i].l-1]));
    }
    printf("%d",ans);
}