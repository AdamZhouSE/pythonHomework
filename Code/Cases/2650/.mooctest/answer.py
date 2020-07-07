#include<bits/stdc++.h>
#define il inline
#define ll long long
#define lson l,m,rt<<1
#define rson m+1,r,rt<<1|1
using namespace std;
const int N=300005;
int tr[N<<2],n,m,pos[N],a[N],ans[N];
struct node{
    int l,r,k,id;
}q[N];
struct numm{
    int v,id;
    bool operator < (const numm a)const{return v<a.v;}
}nm[N];
il bool cmp(node a,node b){return pos[a.l]==pos[b.l]?a.r<b.r:a.l<b.l;}
il int gi(){
    int a=0;char x=getchar();bool f=0;
    while((x<'0'||x>'9')&&x!='-')x=getchar();
    if(x=='-')x=getchar(),f=1;
    while(x>='0'&&x<='9')a=a*10+x-48,x=getchar();
    return f?-a:a;
}
il void pushup(int rt){tr[rt]=tr[rt<<1]+tr[rt<<1|1];}
il void update(int k,int c,int l,int r,int rt){
    if(l==k&&r==k){tr[rt]+=c;return;}
    tr[rt]+=c;
    int m=l+r>>1;
    if(k<=m)update(k,c,lson);
    else update(k,c,rson);
    pushup(rt);
}
il int query(int k,int l,int r,int rt){
    if(l==r)return l;
    int m=l+r>>1;
    if(tr[rt<<1]>=k)return query(k,lson);
    else return query(k-tr[rt<<1],rson);
}
int main(){
    n=gi(),m=gi();
    int s=int(sqrt(n));
    for(int i=1;i<=n;i++)nm[i].v=gi(),nm[i].id=i,pos[i]=(i-1)/s+1;
    sort(nm+1,nm+n+1);
    for(int i=1;i<=n;i++)a[nm[i].id]=i;
    for(int i=1;i<=m;i++)q[i].l=gi(),q[i].r=gi(),q[i].k=gi(),q[i].id=i;
    sort(q+1,q+m+1,cmp);
    for(int i=1,l=1,r=0;i<=m;i++){
        while(r<q[i].r)update(a[++r],1,1,n,1);
        while(r>q[i].r)update(a[r--],-1,1,n,1);
        while(l<q[i].l)update(a[l++],-1,1,n,1);
        while(l>q[i].l)update(a[--l],1,1,n,1);
        ans[q[i].id]=nm[query(q[i].k,1,n,1)].v;
    }
    for(int i=1;i<=m;i++)printf("%d\n",ans[i]);
    return 0;
}