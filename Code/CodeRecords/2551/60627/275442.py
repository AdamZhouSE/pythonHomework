#include<bits/stdc++.h>
#define N 1000005
#define LL long long
#define RE register
#define IN inline

using namespace std;

IN void in(int &x){
    int flg=1;RE char ch=getchar();x=0;
    for(;ch>'9'||ch<'0';){if(ch=='-') flg=-1;ch=getchar();}
    for(;ch<='9'&&ch>='0';ch=getchar()) x=x*10+ch-'0';
    x*=flg;
}

struct node{
    int l,r,w,f;
}tr[N];
int n,m,ans,X,tot;
int e[N];

IN void build(int k,int l,int r){
    tr[k].l=l;tr[k].r=r;
    if(l==r){
        tr[k].w=e[l];
        return;
    }int mid=(l+r)/2;
    build(k*2,l,mid);build(k*2+1,mid+1,r);
    tr[k].w=tr[k*2].w+tr[k*2+1].w;
}

IN void down(int k){
    tr[k].f^=1;
    tr[k*2].w=(tr[k*2].r-tr[k*2].l+1)-tr[k*2].w;
    tr[k*2+1].w=(tr[k*2+1].r-tr[k*2+1].l+1)-tr[k*2+1].w;
    tr[k*2].f^=1;
    tr[k*2+1].f^=1;
}

IN void ask_interval(int k,int l,int r){
    int ll=tr[k].l,rr=tr[k].r,mid=(ll+rr)/2;
    if(ll>=l&&rr<=r){
        ans+=tr[k].w;
        return;
    }if(tr[k].f) down(k);
    if(l<=mid) ask_interval(k*2,l,r);
    if(r>mid) ask_interval(k*2+1,l,r);
    tr[k].w=tr[k*2].w+tr[k*2+1].w;
}

IN void change_interval(int k,int l,int r){
    int ll=tr[k].l,rr=tr[k].r,mid=(ll+rr)/2;
    if(ll>=l&&rr<=r){
        tr[k].w=(rr-ll+1)-tr[k].w;
        tr[k].f^=1;
        return;
    }if(tr[k].f) down(k);
    if(l<=mid) change_interval(k*2,l,r);
    if(r>mid) change_interval(k*2+1,l,r);
    tr[k].w=tr[k*2].w+tr[k*2+1].w;
}

int main()
{
    in(n);in(m);
    build(1,1,n);
    while(m--){
        int p,l,r;
        in(p);in(l);in(r);
        if(p==0){
            change_interval(1,l,r);
        }else {
            ans=0,ask_interval(1,l,r);
            printf("%d\n",ans);
        }
    }return 0;
}