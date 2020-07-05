#include<iostream>
#include<algorithm>
#include<cstdio>
#define MAXN 100010
using namespace std;
int n,m,k,c=1,d=1,last=0;
int w[MAXN],head[MAXN],num[MAXN],root[MAXN],deep[MAXN],f[MAXN][20];
struct node1{
    int l,r,sum;
}a[MAXN*20];
struct node2{
    int next,to;
}b[MAXN<<1];
inline int read(){
    int date=0,w=1;char c=0;
    while(c<'0'||c>'9'){if(c=='-')w=-1;c=getchar();}
    while(c>='0'&&c<='9'){date=date*10+c-'0';c=getchar();}
    return date*w;
}
void pushup(int rt){
    a[rt].sum=a[a[rt].l].sum+a[a[rt].r].sum;
}
void add(int x,int y){
    b[d].to=y;
    b[d].next=head[x];
    head[x]=d++;
    b[d].to=x;
    b[d].next=head[y];
    head[y]=d++;
}
void insert(int k,int v,int l,int r,int &rt){
    int mid;
    a[c++]=a[rt];rt=c-1;
    if(l==k&&k==r){
        a[rt].sum+=v;
        return;
    }
    mid=l+r>>1;
    if(k<=mid)insert(k,v,l,mid,a[rt].l);
    else insert(k,v,mid+1,r,a[rt].r);
    pushup(rt);
}
void buildtree(int rt){
    int will;
    for(int i=head[rt];i;i=b[i].next){
        will=b[i].to;
        if(!deep[will]){
            deep[will]=deep[rt]+1;
            int x=lower_bound(num+1,num+k+1,w[will])-num;
            root[will]=root[rt];
            insert(x,1,1,k,root[will]);
            f[will][0]=rt;
            buildtree(will);
        }
    }
}
void step(){
    for(int i=1;i<=19;i++)
    for(int j=1;j<=n;j++)
    f[j][i]=f[f[j][i-1]][i-1];
}
int query(int i,int j,int fa,int fafa,int k,int l,int r){
    if(l==r)return l;
    int mid=l+r>>1,t=a[a[i].l].sum+a[a[j].l].sum-a[a[fa].l].sum-a[a[fafa].l].sum;
    if(k<=t)return query(a[i].l,a[j].l,a[fa].l,a[fafa].l,k,l,mid);
    else return query(a[i].r,a[j].r,a[fa].r,a[fafa].r,k-t,mid+1,r);
}
int LCA(int x,int y){
    if(deep[x]<deep[y])swap(x,y);
    for(int i=19;i>=0;i--)
    if(deep[f[x][i]]>=deep[y])
    x=f[x][i];
    if(x==y)return x;
    for(int i=19;i>=0;i--)
    if(f[x][i]!=f[y][i]){
        x=f[x][i];
        y=f[y][i];
    }
    return f[x][0];
}
void work(int u,int v,int q){
    int fa=LCA(u,v);
	last=num[query(root[u],root[v],root[fa],root[f[fa][0]],q,1,k)];
    printf("%d\n",last);
}
int main(){
    int u,v,q;
    n=read();m=read();
    a[0].l=a[0].r=a[0].sum=0;
    root[0]=0;
    for(int i=1;i<=n;i++){
        w[i]=read();
        num[i]=w[i];
    }
    sort(num+1,num+n+1);
    k=unique(num+1,num+n+1)-num-1;
    for(int i=1;i<n;i++){
        u=read();v=read();
        add(u,v);
    }
	u=lower_bound(num+1,num+k+1,w[1])-num;
	insert(u,1,1,k,root[1]);
    deep[1]=1;
    buildtree(1);
    step();
    while(m--){
        u=read();v=read();q=read();
        u^=last;
        work(u,v,q);
    }
    return 0;
}