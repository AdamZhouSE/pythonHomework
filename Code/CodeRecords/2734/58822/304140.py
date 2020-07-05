#include<bits/stdc++.h>
#include<cctype>
#include<algorithm>
#include<deque>
#define For(i,a,b) for(i=(a);i<=(b);++i)
#define Forward(i,a,b) for(i=(a);i>=(b);--i)
using namespace std;
template<typename T>inline void read(T &x)//快读
{
    T s=0,f=1;char k=getchar();
    while(!isdigit(k)&&(k^'-'))k=getchar();
    if(!isdigit(k)){f=-1;k=getchar();}
    while(isdigit(k)){s=s*10+(k^48);k=getchar();}
    x=s*f;
}
const int MAXN=100010;
int n,m,c,head[MAXN],e;//head是主席树的根数组
struct node
{
    int l,r,count;
}p[MAXN<<4];//节点
void make_tree(int poi,int l,int r)//建立空树
{
    if(l==r)return;
    int mid=(l+r)>>1;
    make_tree(p[poi].l=++e,l,mid);
    make_tree(p[poi].r=++e,mid+1,r);
}
void build(int now,int last,int l,int r,int x)//加入新树
{
    if(l==r)
    {
        p[now].count=p[last].count+1;
        return;
    }
    int mid=(l+r)>>1;
    if(x<=mid)
    {
        p[now].r=p[last].r;
        build(p[now].l=++e,p[last].l,l,mid,x);
    }
    else
    {
        p[now].l=p[last].l;
        build(p[now].r=++e,p[last].r,mid+1,r,x);
    }
    p[now].count=p[p[now].l].count+p[p[now].r].count;
}
int query(int now,int last,int l,int r)//查询
{
    //printf("%d %d %d\n",l,r,p[now].count-p[last].count);
    if(p[now].count-p[last].count<2)return 0;
    if(l==r)return 1;
    int mid=(l+r)>>1,ans=0;
    ans=query(p[now].l,p[last].l,l,mid)+query(p[now].r,p[last].r,mid+1,r);
    return ans;
}
int main(void)
{
    read(n);
    read(c);
    read(m);
    int i,l,r,k;
    make_tree(head[0]=++e,1,c);//先建一颗空树作为基础树
    For(i,1,n)read(k),build(head[i]=++e,head[i-1],1,c,k);//再在空树的基础上log2n地更新节点
    while(m--)
    {
        read(l),read(r);
        printf("%d\n",query(head[r],head[l-1],1,c));//查询
    }
    return 0;
}