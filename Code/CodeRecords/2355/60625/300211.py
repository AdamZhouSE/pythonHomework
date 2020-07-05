#include<cstdio>
#include<iostream>
#include<cstring>
#include<algorithm>
#include<cmath>
using namespace std;
struct node
{
    int f,d,c,n,son[2],mx,ad;
    bool fz;
}tr[310000];
void add(int x)
{
    tr[x].d+=tr[x].ad;tr[x].mx+=tr[x].ad;
    int lc=tr[x].son[0],rc=tr[x].son[1];
    tr[lc].ad+=tr[x].ad;
    tr[rc].ad+=tr[x].ad;
    tr[x].ad=0;
}
void update(int x)
{
    int lc=tr[x].son[0],rc=tr[x].son[1];
    tr[x].c=tr[lc].c+tr[rc].c+tr[x].n;
    if(tr[lc].ad!=0)add(lc);
    if(tr[rc].ad!=0)add(rc);
    if(lc==0)tr[lc].mx=0;
    if(rc==0)tr[rc].mx=0;
    tr[x].mx=max(max(tr[lc].mx,tr[rc].mx),tr[x].d);
}
void reverse(int x)
{
    tr[x].fz=false;
    swap(tr[x].son[0],tr[x].son[1]);
    int lc=tr[x].son[0],rc=tr[x].son[1];
    tr[lc].fz=1-tr[lc].fz;
    tr[rc].fz=1-tr[rc].fz;
}
void rotate(int x,int w)
{
    int f=tr[x].f,ff=tr[f].f;
    int R,r;

    R=f;r=tr[x].son[w];
    tr[R].son[1-w]=r;
    if(r!=0)tr[r].f=R;

    R=ff;r=x;
         if(tr[R].son[0]==f)tr[R].son[0]=r;
    else if(tr[R].son[1]==f)tr[R].son[1]=r;
    tr[r].f=R;

    R=x;r=f;
    tr[R].son[w]=r;
    tr[r].f=R;

    update(f);
    update(x);
}
int tmp[310000];
void splay(int x,int rt)
{
    int s=0,i=x;
    while(tr[i].f!=0&&(tr[tr[i].f].son[0]==i||tr[tr[i].f].son[1]==i))
    {
        tmp[++s]=i;
        i=tr[i].f;
    } 
    tmp[++s]=i;
    while(s!=0)
    {
        i=tmp[s];s--;
        if(tr[i].fz==true)reverse(i);
        if(tr[i].ad!=0)add(i);
    }

    while(tr[x].f!=rt&&(tr[tr[x].f].son[0]==x||tr[tr[x].f].son[1]==x))//还有虚边啊！
    {
        int f=tr[x].f,ff=tr[f].f;
        if(ff==rt||(tr[ff].son[0]!=f&&tr[ff].son[1]!=f))
        {
            if(x==tr[f].son[0])rotate(x,1);
            else               rotate(x,0);
        }
        else
        {
                 if(tr[f].son[0]==x&&tr[ff].son[0]==f){rotate(f,1);rotate(x,1);}
            else if(tr[f].son[1]==x&&tr[ff].son[0]==f){rotate(x,0);rotate(x,1);}
            else if(tr[f].son[0]==x&&tr[ff].son[1]==f){rotate(x,1);rotate(x,0);}
            else if(tr[f].son[1]==x&&tr[ff].son[1]==f){rotate(f,0);rotate(x,0);}
        }
    }
}
int n,w[310000];
void make_tree()
{
    for(int i=0;i<=n;i++)
    {
        tr[i].f=0;
        tr[i].mx=tr[i].d=w[i];
        tr[i].c=1;tr[i].n=1;
        tr[i].son[0]=tr[i].son[1]=0;
        tr[i].fz=false;tr[i].ad=0;
    }
}
void access(int x)//访问x 
//还记得树剖的重儿子吗？这是令点x到整棵动态树的根这条路径变成偏爱路径(相当于树剖的重链)，这一条路径就是一棵伸展树。 
{
    int y=0;
    while(x!=0)
    {
        splay(x,0);
        tr[x].son[1]=y;
        if(y!=0)tr[y].f=x;
        y=x;x=tr[x].f;
    }
}
void makeroot(int x)//让x成为当前树的根
{
    access(x);splay(x,0);//因为是链，splay之后只有左孩子(上面y=0) 
    tr[x].fz=1-tr[x].fz;//因为要让x成为整棵树的根，所以x的深度要最小(通过翻转实现),为find_root做准备
}
void link(int x,int y)
{//为什么可以直接用makeroot？？因为判断过x和y的find_root 是否相同，不相同表示x和y是不联通的
    makeroot(x);tr[x].f=y;access(x);//删去access是没有影响的，但从定义上说应该加上 
}
void cut(int x,int y)
{
    makeroot(x);
    access(y);splay(y,0);
    tr[tr[y].son[0]].f=0;tr[y].son[0]=0;
    update(y);
}
int find_root(int x)//访问完x后，x所属的伸展树的最左端的点就是所在树真正的根，因为伸展树实际意义上就是一条链啊！！ 
{
    access(x);splay(x,0);
    while(tr[x].son[0]!=0)x=tr[x].son[0];
    return x;
}
void increase(int x,int y,int W)//令x，y处于一棵伸展树，y为根，由于是链，直接更新y的ad就行了 
{
    makeroot(x);
    access(y);splay(y,0);
    tr[y].ad+=W;
}
int findmax(int x,int y)//同理，这也是一样的 
{
    makeroot(x);
    access(y);splay(y,0);
    update(y);return tr[y].mx;
}
struct edge
{
    int x,y;
}e[310000];
int main()
{
    freopen("weight.in","r",stdin);
    freopen("weight.out","w",stdout);
    int m,op,x,y,W;
    while(scanf("%d",&n)!=EOF)
    {
        for(int i=1;i<n;i++)scanf("%d%d",&e[i].x,&e[i].y);
        for(int i=1;i<=n;i++)scanf("%d",&w[i]);
        make_tree();
        for(int i=1;i<n;i++)
            link(e[i].x,e[i].y);
        scanf("%d",&m);
        for(int i=1;i<=m;i++)
        {
            scanf("%d",&op);
            if(op==1)
            {
                scanf("%d%d",&x,&y);
                if(find_root(x)==find_root(y)||x==y)
                    printf("-1\n");
                else 
                    link(x,y);
            }
            else if(op==2)
            {
                scanf("%d%d",&x,&y);
                if(find_root(x)!=find_root(y)||x==y)
                    printf("-1\n");
                else 
                    cut(x,y);
            }
            else if(op==3)
            {
                scanf("%d%d%d",&W,&x,&y);
                if(find_root(x)!=find_root(y))
                    printf("-1\n");
                else 
                    increase(x,y,W);
            }
            else 
            {
                scanf("%d%d",&x,&y);
                if(find_root(x)!=find_root(y))
                    printf("-1\n");
                else 
                    printf("%d\n",findmax(x,y));
            }
        }
        printf("\n");
    }
    return 0;
}