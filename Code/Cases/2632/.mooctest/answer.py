#include<cstdio>
#include<iostream>
#include<cstring>
using namespace std;
int op=0;
int h[500000];
int n,m,ans,a,anst;
int sl[500000];
int cc1,cc2;
char si;
struct house
{
    int l;
    int r;
    int v;
};
struct house T[500001*4];
//建树 
void buildtree(int f,int ne,int poi)
{
    T[poi].l=f;
    T[poi].r=ne;
    if(f==ne)
    {
        T[poi].v=h[f];
        return ;
    }
    buildtree(f,(f+ne)/2,poi*2);
    buildtree((f+ne)/2+1,ne,poi*2+1);
    T[poi].v=(T[poi*2].v+T[poi*2+1].v);
}
//修改操作 
void insert(int go,int val,int poi)
{
    if(T[poi].l==go&&T[poi].r==go)
    {
        T[poi].v=val;
        h[go]=val;    
        return ;
    }
    int mid=(T[poi].l+T[poi].r)/2;
    if(go>mid) insert(go,val,poi*2+1);
    else if(go<=mid) insert(go,val,poi*2);
    T[poi].v=T[poi*2].v+T[poi*2+1].v;
}
/*
qh函数用来计算要找的区间中完好的房子数

（就是一个线段树区间查询啦）

*/
void qh(int f,int ne,int poi)
{
    if(T[poi].l==f&&T[poi].r==ne)
    {
        anst+=T[poi].v;
        return ;
    }
    int mid=(T[poi].l+T[poi].r)/2;
    if(f>mid) qh(f,ne,poi*2+1);
    else if(ne<=mid) qh(f,ne,poi*2);
    else 
    {
        qh(f,mid,poi*2);
        qh(mid+1,ne,poi*2+1);
    }
}
void search1(int f,int ne,int poi)
{
    if(T[poi].l==f&&T[poi].r==ne&&T[poi].v==0&&f==ne)
    {
        cc1=f;//找到了在询问点左端最近的一个零 
        return ;
    }
    if(T[poi].l==f&&T[poi].r==ne&&T[poi].v==1&&f==ne)
    {
        cc1=0;//这里有一个特判，如果找到最后，发现左边所有的点都是1，那么最左边记为0 
        return ;
    }
    int mid=(T[poi].r+T[poi].l)/2;
    if(f>mid) search1(f,ne,poi*2+1);
    else if(ne<=mid) search1(f,ne,poi*2);
    else 
    {
        anst=0;
        qh(T[poi*2+1].l,ne,poi);//因为我们找的是最左边的那个，所以如果现在所在的节点左右子树中都有零，优先往右跳 
        if(anst<ne-T[poi*2+1].l+1)
            search1(mid+1,ne,poi*2+1);//往右跳，继续递归 
        else search1(f,mid,poi*2);
    }
}
//对于寻找在询问点右边最近为零的点，道理同上 
void search2(int f,int ne,int poi)
{
    if(T[poi].l==f&&T[poi].r==ne&&T[poi].v==0&&f==ne)
    {
        cc2=f;
        return ;
    }
    if(T[poi].l==f&&T[poi].r==ne&&T[poi].v==1&&f==ne)
    {
        cc2=n+1;
        return ;
    }
    int mid=(T[poi].l+T[poi].r)/2;
    if(f>mid) search2(f,ne,poi*2+1);
    else if(ne<=mid) search2(f,ne,poi*2);
    else 
    {
        anst=0;
        qh(f,T[poi*2].r,poi);
        if(anst<T[poi*2].r-f+1)//if(anst<T[poi*2].r-f+1)
            search2(f,mid,poi*2);
        else search2(mid+1,ne,poi*2+1);
    }
}
int main()
{
    scanf("%d%d",&n,&m);
    for(int i=1;i<=n;i++)
    {
        h[i]=1;
    }
    buildtree(1,n,1);
    for(int i=1;i<=m;i++)
    {
        cin>>si;
        //scanf("%c",&si);
        if(si=='D')
        {
            scanf("%d",&a);
            insert(a,0,1);
            sl[++op]=a;
        }
        if(si=='Q')
        {
            ans=0;
            scanf("%d",&a);
            if(!h[a])
            {
                printf("0\n");
                continue ;
            }
            if(a==1) 
            {
                search2(a+1,n,1);
                cc1=0;
            }
            else if(a==n)
            {
                search1(1,a-1,1);
                cc2=n+1;
            }
            else
            {
                search1(1,a-1,1);
                //printf("* %d *",cc1);
                search2(a+1,n,1);
                //printf("* %d *",cc2);
            }
            printf("%d\n",cc2-cc1-1);
        }
        if(si=='R')
        {
            int t=sl[op--];
            insert(t,1,1);
        }
    }
    return 0;
}