#include<cstdio>
#include<algorithm>
#include<cmath>
#include<cctype>
using namespace std;
typedef long long LL;
const int N=3e5+5,mo=998244353;
int tot;
int first[N],nex[N<<1],en[N<<1];
int dep[N],q[N],f[N][19],g[N][51];
inline int read()
{
    int X=0,w=0; char ch=0;
    while(!isdigit(ch)) w|=ch=='-',ch=getchar();
    while(isdigit(ch)) X=(X<<1)+(X<<3)+(ch^48),ch=getchar();
    return w?-X:X;
}
inline void write(int x)
{
    if(x>9) write(x/10);
    putchar(x%10+'0');
}
inline void insert(int x,int y)
{
    nex[++tot]=first[x];
    first[x]=tot;
    en[tot]=y;
}
void dfs(int x)
{
    dep[x]=dep[f[x][0]]+1;
    for(int i=first[x];i;i=nex[i])
        if(en[i]^f[x][0])
        {
            f[en[i]][0]=x;
            dfs(en[i]);
        }
}
inline int ksm(int x,int y)
{
    int s=1;
    while(y)
    {
        if(y&1) s=(LL)s*x%mo;
        x=(LL)x*x%mo;
        y>>=1;
    }
    return s;
}
inline int getlca(int x,int y)
{
    if(dep[x]<dep[y]) swap(x,y);
    for(int i=log2(dep[x]);i>=0;i--)
        if(dep[f[x][i]]>=dep[y]) x=f[x][i];
    if(x==y) return x;
    for(int i=log2(dep[x]);i>=0;i--)
        if(f[x][i]^f[y][i]) x=f[x][i],y=f[y][i];
    return f[x][0];
}
int main()
{
    freopen("sum.in","r",stdin);
    freopen("sum.out","w",stdout);
    int n=read();
    for(int i=1;i<n;i++)
    {
        int x=read(),y=read();
        insert(x,y);
        insert(y,x);
    }
    int l=0,r=q[1]=dep[1]=1;
    while(l<r)
    {
        int x=q[++l];
        for(int i=first[x];i;i=nex[i])
            if(en[i]^f[x][0])
            {
                f[en[i]][0]=x;
                dep[en[i]]=dep[x]+1;
                q[++r]=en[i];
            }
    }
    //dfs(1);
    for(int j=1;j<=50;j++)
        for(int i=1;i<=n;i++)
            g[i][j]=(g[i-1][j]+ksm(i-1,j))%mo;
    for(int j=1;j<19;j++)
        for(int i=1;i<=n;i++)
            f[i][j]=f[f[i][j-1]][j-1];
    int m=read();
    while(m--)
    {
        int x=read(),y=read(),k=read();
        int z=getlca(x,y);
        int ans=(g[dep[x]][k]+g[dep[y]][k])%mo;
        ans=(ans-(LL)2*g[dep[z]][k]%mo+mo)%mo;
        int sum=((LL)g[dep[z]][k]-g[dep[z]-1][k]+mo)%mo;
        ans=(ans+sum)%mo;
        write(ans),putchar('\n');
    }
    return 0;
}