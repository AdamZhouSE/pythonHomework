#include <cstdio>
#include <algorithm>
#define ls t[now].ch[0]
#define rs t[now].ch[1]
#define f t[now].par
const int N=100010;
struct node
{
    int dat,index;
    bool friend operator <(node n1,node n2)
    {
        return n1.dat<n2.dat;
    }
}a[N];
struct BST
{
    int ch[2],dat,index,par;//左右儿子，BST域，堆域，父亲
}t[N];
int tot=0,n,s[N];
void connect(int fa,int now,int typ)
{
    f=fa;
    t[fa].ch[typ]=now;
}
void dfs(int now)
{
    if(!now) return;
    printf("%d ",t[now].dat);
    dfs(ls);
    dfs(rs);
}
int main()
{
    scanf("%d",&n);
    for(int i=1;i<=n;i++)
    {
        scanf("%d",a+i);
        a[i].index=i;
    }
    std::sort(a+1,a+1+n);
    for(int i=1;i<=n;i++)
    {
        int last=0;
        while(tot&&t[s[tot]].index>a[i].index)
            last=tot--;
        t[i].dat=a[i].dat;
        t[i].index=a[i].index;
        connect(s[tot],i,1);
        connect(i,s[last],0);
        s[++tot]=i;
    }
    dfs(t[0].ch[1]);
    return 0;
}