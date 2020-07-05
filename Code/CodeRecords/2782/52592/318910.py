#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<iostream>
#include<algorithm>
#include<cmath>
using namespace std;
const int inf=0x3f3f3f3f;
struct zk
{
    int cnt,fa,son[2],val;
}tree[50001];
int root=0;
int inx=0;
void rotate(int x)
{
    int y=tree[x].fa,z=tree[y].fa,o=(x==tree[y].son[1]);
    tree[y].son[o]=tree[x].son[o^1];
    tree[tree[x].son[o^1]].fa=y;
    tree[x].son[o^1]=y; tree[y].fa=x;
 
    tree[z].son[tree[z].son[1]==y]=x;
    tree[x].fa=z;
}
void splay(int x)
{
    for(int y;y=tree[x].fa;rotate(x))
    {
        if (tree[y].fa)
        { 
            rotate(((tree[y].son[0]==x)==(tree[tree[y].fa].son[0]==y))?y:x);
        }
    }
    root=x;
}
void insert(int x,int a)
{
    int y=0;
    while(x&&tree[x].val!=a)
    {
        y=x;
        x=tree[x].son[tree[x].val<a];
    }
    if (x) tree[x].cnt++;
    else 
    {
        inx++;
        x=inx;
        tree[x].cnt=1;
        tree[inx].fa=y;
        tree[inx].val=a;
        tree[y].son[a>tree[y].val]=x;
    }   
    splay(x);
}
int fro,beh;
void pre(int x,int a)
{
    if (!x) return;
    if (tree[x].val<=a)
    {
        fro=x;
        pre(tree[x].son[1],a);
    }
    else pre(tree[x].son[0],a);
}
void suc(int x,int a)
{
    if (!x) return;
    if (tree[x].val>=a)
    {
        beh=x;
        suc(tree[x].son[0],a);
    }
    else suc(tree[x].son[1],a);
}
int n;
int main()
{
    int a,ans=0;
    scanf("%d%d",&n,&a);
    insert(root,inf);
    insert(root,-inf);
    insert(root,a);
    ans+=abs(a);
    for(int i=2;i<=n;i++)
    {
        scanf("%d",&a);
        
        pre(root,a);suc(root,a);
        ans+=min(abs(a-tree[fro].val),abs(tree[beh].val-a));insert(root,a);
    }
    printf("%d",ans);
    return 0;
}
