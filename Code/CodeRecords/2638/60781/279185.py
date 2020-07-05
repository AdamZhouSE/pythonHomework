#include<iostream>
#include<cstring>
#include<cstdio>
using namespace std;
#define MAXN 100050
#define INF 0
struct Segment_Tree{
    int l,r;
    double sum,sum_squ,p,lazy;
}tre[MAXN<<2];
inline void UpDate(int u){
    tre[u].sum=tre[u<<1].sum+tre[u<<1|1].sum;
    tre[u].sum_squ=tre[u<<1].sum_squ+tre[u<<1|1].sum_squ;
    tre[u].p=tre[u].sum/(tre[u].r-tre[u].l+1);
}
#define lc u<<1
#define rc u<<1|1
inline void PushDown(int u){
    tre[lc].lazy+=tre[u].lazy,tre[rc].lazy+=tre[u].lazy;

    int n=tre[lc].r-tre[lc].l+1; double z=tre[u].lazy;
    tre[lc].sum_squ+=n*(z*2*tre[lc].p+z*z);
    tre[lc].p+=z,tre[lc].sum+=n*z;

    n=tre[rc].r-tre[rc].l+1; z=tre[u].lazy;
    tre[rc].sum_squ+=n*(z*2*tre[rc].p+z*z);
    tre[rc].p+=z,tre[rc].sum+=z*n;
    tre[u].lazy=INF;
}

void Build(int u,int l,int r){
    tre[u].l=l,tre[u].r=r,tre[u].lazy=INF;
    if(l==r){
        scanf("%lf",&tre[u].sum);
        tre[u].sum_squ=tre[u].sum*tre[u].sum;
        tre[u].p=tre[u].sum;
        return ;
    }
    int Mid=l+r>>1;
    Build(u<<1,l,Mid),Build(u<<1|1,Mid+1,r);
    UpDate(u);
}

void Modify(int u,int l,int r,double k){
    if(l<=tre[u].l&&tre[u].r<=r){
        tre[u].lazy+=k;
        tre[u].sum+=(tre[u].r-tre[u].l+1)*k;
        tre[u].sum_squ+=(tre[u].r-tre[u].l+1)*(k*2*tre[u].p+k*k);
        tre[u].p+=k;
        return ;
    }
    if(tre[u].lazy!=INF) PushDown(u);
    int Mid=(tre[u].l+tre[u].r)>>1;
    if(r<=Mid) Modify(u<<1,l,r,k);
    else if(l>Mid) Modify(u<<1|1,l,r,k);
    else Modify(u<<1,l,Mid,k),Modify(u<<1|1,Mid+1,r,k);
    UpDate(u);
}

double query(int u,int l,int r,int opt){
    if(l<=tre[u].l&&tre[u].r<=r){
        if(opt==2) return tre[u].sum;
        if(opt==3) return tre[u].sum_squ;
    }
    if(tre[u].lazy!=INF) PushDown(u);
    int Mid=tre[u].l+tre[u].r>>1;
    if(l>Mid) return query(u<<1|1,l,r,opt);
    else if(r<=Mid) return query(u<<1,l,r,opt);
    else return query(u<<1,l,Mid,opt)+query(u<<1|1,Mid+1,r,opt);
}

int main(){
    int n,m;
    scanf("%d%d",&n,&m);
    Build(1,1,n);

    for(int l,r,opt,i=1;i<=m;++i){
        double k;
        scanf("%d%d%d",&opt,&l,&r);
        int kk=(r-l+1);
        if(opt==1) scanf("%lf",&k),Modify(1,l,r,k);
        if(opt==2)
            printf("%.4lf\n",query(1,l,r,opt)/(r-l+1));
        if(opt==3){
            double sum_square=query(1,l,r,opt);//该区间的平方和 
            double Average=query(1,l,r,2);//该区间的平均值 
            Average/=kk;
            printf("%.4lf\n",(sum_square-kk*Average*Average)/kk);
        }
    }
    return 0;
}
