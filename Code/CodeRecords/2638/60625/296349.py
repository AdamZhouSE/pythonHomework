#include<bits/stdc++.h>
using namespace std;
const int maxn=1e5+5;
int n,m,t,x,y;
double z;
struct data{
    int l,r;
    double sum,ssum,add;
}tree[maxn<<2];
void update(int k)
{
    tree[k].sum=tree[k<<1].sum+tree[k<<1|1].sum;
    tree[k].ssum=tree[k<<1].ssum+tree[k<<1|1].ssum;
}
void pushdown(int k,int x)
{
    if(tree[k].add){
        tree[k<<1].ssum+=2*tree[k].add*tree[k<<1].sum+tree[k].add*tree[k].add*(x-x/2);
        tree[k<<1|1].ssum+=2*tree[k].add*tree[k<<1|1].sum+tree[k].add*tree[k].add*(x/2);
        tree[k<<1].sum+=(x-x/2)*tree[k].add;
        tree[k<<1|1].sum+=(x/2)*tree[k].add;
        tree[k<<1].add+=tree[k].add;
        tree[k<<1|1].add+=tree[k].add;
        tree[k].add=0;
    }
}
void build(int k,int s,int t)
{
    tree[k].l=s;tree[k].r=t;
    if(s==t){scanf("%lf",&tree[k].sum);tree[k].ssum=tree[k].sum*tree[k].sum;return ;}
    int mid=(s+t)>>1;
    build(k<<1,s,mid);
    build(k<<1|1,mid+1,t);
    update(k);
}
void change(int k,int p,int q,double y)
{
    int l=tree[k].l,r=tree[k].r;
    if(l==p&&r==q){
        tree[k].ssum+=2*y*tree[k].sum+(r-l+1)*y*y;
        tree[k].sum+=(r-l+1)*y;
        tree[k].add+=y;
        return ;
    }
    pushdown(k,r-l+1);
    int mid=(l+r)>>1;
    if(q<=mid)change(k<<1,p,q,y);
    else if(p>mid)change(k<<1|1,p,q,y);
    else{
        change(k<<1,p,mid,y);
        change(k<<1|1,mid+1,q,y);
    }
    update(k);
}
double ask1(int k,int p,int q)
{
    int l=tree[k].l,r=tree[k].r;
    if(l==p&&r==q)return tree[k].sum;
    pushdown(k,r-l+1);
    int mid=(l+r)>>1;
    if(q<=mid)return ask1(k<<1,p,q);
    else if(p>mid)return ask1(k<<1|1,p,q);
    else{
        return ask1(k<<1,p,mid)+ask1(k<<1|1,mid+1,q);
    }
}
double ask2(int k,int p,int q)
{
    int l=tree[k].l,r=tree[k].r;
    if(l==p&&r==q)return tree[k].ssum;
    pushdown(k,r-l+1);
    int mid=(l+r)>>1;
    if(q<=mid)return ask2(k<<1,p,q);
    else if(p>mid)return ask2(k<<1|1,p,q);
    else{
        return ask2(k<<1,p,mid)+ask2(k<<1|1,mid+1,q);
    }
}
int main()
{
    scanf("%d%d",&n,&m);
    build(1,1,n);
    for(int i=0;i<m;i++){
        scanf("%d",&t);
        if(t==1){
            scanf("%d%d%lf",&x,&y,&z);
            change(1,x,y,z);
        }else if(t==2){
            scanf("%d%d",&x,&y);
            double ans=ask1(1,x,y)/(y-x+1);
            printf("%.4f\n",ans);
        }else{
            scanf("%d%d",&x,&y);
            double sum=ask1(1,x,y),ssum=ask2(1,x,y),ave=sum/(y-x+1);
            double ans=(ssum-2*ave*sum+(y-x+1)*ave*ave)/(y-x+1);
            printf("%.4f\n",ans);
        }
    }
    return 0;
}

