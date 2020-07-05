#include<cstdio>
#include<algorithm>
#include<iostream>
using namespace std;
const int Logn=20;
const int N=201000;
const int INF=0x3f3f3f3f;
const int M=4100000;
struct Array{
    int x,idx;
    bool operator < (const Array &rhs) const{
        return x<rhs.x;
    }
}a[N];
struct TreeNode{
    int L,R,sum;
}T[M];
struct Edge{
    int to,next;
}e[N*2];
int b[N],head[N],root[N],fa[N][Logn+5],rank[N],dep[N];
int tn,n,m,EdgeCnt=0,T_cnt=1;
int read(){
    int x=0,f=1;char ch=getchar();
    while (ch<'0' || ch>'9'){if (ch=='-')f=-1;ch=getchar();}
    while ('0'<=ch && ch<='9'){x=(x<<3)+(x<<1)+(ch^48);ch=getchar();}
    return x*f;
}
void write(int x){
    if (x<0)x=-x;
    if (x>=10)write(x/10);
    putchar(x%10+48);
}
void addedge(int u,int v){
    int p=++EdgeCnt;
    e[p].to=v;e[p].next=head[u];
    head[u]=p;
}
void insert(int &now,int val,int l=1,int r=tn){
    T[T_cnt++]=T[now];now=T_cnt-1;
    T[now].sum++;
    if (l==r)return;
    int mid=(l+r)>>1;
    if (val<=mid)insert(T[now].L,val,l,mid);
        else insert(T[now].R,val,mid+1,r);
}
int query(int a,int b,int c,int d,int k,int l=1,int r=tn){
    if (l==r)return l;
    int t=T[T[a].L].sum+T[T[b].L].sum-T[T[c].L].sum-T[T[d].L].sum;
    int mid=(l+r)>>1;
    if (k<=t)return query(T[a].L,T[b].L,T[c].L,T[d].L,k,l,mid);
        else return query(T[a].R,T[b].R,T[c].R,T[d].R,k-t,mid+1,r);
}
void dfs(int u){
    root[u]=root[fa[u][0]];
    insert(root[u],rank[u]);
    for (int p=head[u];p;p=e[p].next){
        int v=e[p].to;
        if (v!=fa[u][0]){
            fa[v][0]=u;
            dep[v]=dep[u]+1;
            dfs(v);
        }
    }
}
int LCA(int u,int v){
    if (dep[u]<dep[v])swap(u,v);
    for (int k=Logn-1;k>=0;k--)
        if (dep[fa[u][k]]>=dep[v])u=fa[u][k];
    if (u==v)return u;
    for (int k=Logn-1;k>=0;k--)
        if (fa[u][k]!=fa[v][k]){u=fa[u][k],v=fa[v][k];}
    return fa[u][0];
}
int main(){
    n=read(),m=read();
    for (int i=1;i<=n;i++){
        a[i].x=read(),a[i].idx=i;
    }
    sort(a+1,a+n+1);
    a[0].x=-INF;
    for (int i=1;i<=n;i++){
        rank[a[i].idx]=rank[a[i-1].idx]+(a[i].x!=a[i-1].x);
        b[rank[a[i].idx]]=a[i].x;
    }
    tn=rank[a[n].idx];
    for (int i=1;i<n;i++){
        int u=read(),v=read();
        addedge(u,v);addedge(v,u);
    }
    fa[1][0]=0;root[0]=0;dep[1]=1;dfs(1);
    for (int i=1;i<Logn;i++)
        for (int j=1;j<=n;j++)
            fa[j][i]=fa[fa[j][i-1]][i-1];
    int ans=0;
    for (int i=1;i<=m;i++){
        int u=read(),v=read(),k=read();
        u^=ans;
        int tt=LCA(u,v);
        int tmp=query(root[u],root[v],root[tt],root[fa[tt][0]],k);
        ans=b[tmp];
        write(ans);puts("");
    }
    return 0;
}