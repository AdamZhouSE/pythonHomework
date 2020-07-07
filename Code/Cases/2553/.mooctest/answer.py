#include<iostream>
#include<cstring>
#include<cstdio>
#define re register
#define maxn 100005
#define max(a,b) ((a)>(b)?(a):(b))
inline int read()
{
    char c=getchar();
    int x=0;
    while(c<'0'||c>'9') c=getchar();
    while(c>='0'&&c<='9')
        x=(x<<3)+(x<<1)+c-48,c=getchar();
    return x;
}
int ch[maxn][2],a[maxn],n,now,key[maxn];
void dfs(int x)
{
    if(ch[x][0]) dfs(ch[x][0]);
    a[++now]=key[x];
    if(ch[x][1]) dfs(ch[x][1]);
}
int f[maxn],d[maxn],len;
inline int find(int x)
{
    int l=1,r=len,ans=0;
    while(l<=r)
    {
        int mid=l+r>>1;
        if(d[mid]<=x) ans=mid,l=mid+1;
            else r=mid-1;
    }
    return ans;
}
int main()
{
    n=read();
    for(re int i=1;i<=n;i++)
        key[i]=read();
    int x,fa;
    for(re int i=2;i<=n;i++)
        fa=read(),x=read(),ch[fa][x]=i;
    dfs(1);
    for(re int i=1;i<=n;i++)
        a[i]-=i;
    for(re int i=1;i<=n;i++)
    {
        f[i]=find(a[i])+1;
        d[f[i]]=a[i];
        len=max(len,f[i]);
    }
    printf("%d\n",n-len);
    return 0;
}