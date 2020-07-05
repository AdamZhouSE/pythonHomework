#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cmath>
#define MAXN 100010
using namespace std;
int n,m;
int root[MAXN];
char str[MAXN];
int top,sa[MAXN],rk[MAXN],tax[MAXN],tp[MAXN],height[MAXN],f[MAXN][20],Log[MAXN];
inline int read(){
    int date=0,w=1;char c=0;
    while(c<'0'||c>'9'){if(c=='-')w=-1;c=getchar();}
    while(c>='0'&&c<='9'){date=date*10+c-'0';c=getchar();}
    return date*w;
}
namespace CT{
    int size=0;
    struct Chairman_Tree{
        int l,r,sum;
    }a[MAXN*20];
    inline void buildtree(){
        root[0]=a[0].l=a[0].r=a[0].sum=0;
    }
    void insert(int k,int v,int l,int r,int &rt){
        a[++size]=a[rt];rt=size;
        a[rt].sum+=v;
        if(l==r)return;
        int mid=l+r>>1;
        if(k<=mid)insert(k,v,l,mid,a[rt].l);
        else insert(k,v,mid+1,r,a[rt].r);
    }
    int query(int l,int r,int lside,int rside,int i,int j){
        if(a[i].sum==a[j].sum)return 0;
        if(l<=lside&&rside<=r)return (a[j].sum-a[i].sum);
        int mid=lside+rside>>1,ans=0;
        if(l<=mid)ans+=query(l,r,lside,mid,a[i].l,a[j].l);
        if(mid<r)ans+=query(l,r,mid+1,rside,a[i].r,a[j].r);
        return ans;
    }
}
void radixsort(){
    for(int i=0;i<=top;i++)tax[i]=0;
    for(int i=1;i<=n;i++)tax[rk[i]]++;
    for(int i=1;i<=top;i++)tax[i]+=tax[i-1];
    for(int i=n;i>=1;i--)sa[tax[rk[tp[i]]]--]=tp[i];
}
void suffixsort(){
    top=30;
    for(int i=1;i<=n;i++){
        rk[i]=str[i]-'a'+1;
        tp[i]=i;
    }
    radixsort();
    for(int w=1,p=0;p<n;top=p,w<<=1){
        p=0;
        for(int i=1;i<=w;i++)tp[++p]=n-w+i;
        for(int i=1;i<=n;i++)if(sa[i]>w)tp[++p]=sa[i]-w;
        radixsort();
        swap(tp,rk);
        rk[sa[1]]=p=1;
        for(int i=2;i<=n;i++)
        rk[sa[i]]=(tp[sa[i-1]]==tp[sa[i]]&&tp[sa[i-1]+w]==tp[sa[i]+w])?p:++p;
    }
}
void getheight(){
    for(int i=1,j,k=0;i<=n;i++){
        if(k)k--;
        j=sa[rk[i]-1];
        while(str[i+k]==str[j+k])k++;
        height[rk[i]]=k;
    }
}
void step(){
    Log[0]=0;
    for(int i=1;i<=n;i++){
        f[i][0]=height[i];
        Log[i]=log2(i);
    }
    for(int i=1;i<=Log[n];i++)
    for(int j=1;j+(1<<(i-1))<=n;j++)
    f[j][i]=min(f[j][i-1],f[j+(1<<(i-1))][i-1]);
}
inline int query(int l,int r){
    l++;r++;
    int k=Log[r-l];
    return min(f[l][k],f[r-(1<<k)][k]);
}
bool check(int x,int l1,int r1,int l2,int r2){
    int Left,Right;
    int l=1,r=rk[l2];
    while(l<r){
        int mid=l+r>>1;
        if(query(mid,rk[l2])<x)l=mid+1;
        else r=mid;
    }
    Left=r;
    l=rk[l2];r=n;
    while(l<r){
        int mid=l+r+1>>1;
        if(query(rk[l2],mid)<x)r=mid-1;
        else l=mid;
    }
    Right=r;
    if(CT::query(l1,r1-x+1,1,n,root[Left-1],root[Right]))return true;
    return false;
}
inline int solve(int l1,int r1,int l2,int r2){
    int l=0,r=min(r1-l1+1,r2-l2+1);
    while(l<r){
        int mid=l+r+1>>1;
        if(check(mid,l1,r1,l2,r2))l=mid;
        else r=mid-1;
    }
    return r;
}
void work(){
    int l1,l2,r1,r2;
    while(m--){
        l1=read();r1=read();l2=read();r2=read();
        printf("%d\n",solve(l1,r1,l2,r2));
    }
}
void init(){
    n=read();m=read();
    scanf("%s",str+1);
    suffixsort();
    getheight();
    step();
    CT::buildtree();
    for(int i=1;i<=n;i++){
        root[i]=root[i-1];
        CT::insert(sa[i],1,1,n,root[i]);
    }
}
int main(){
    init();
    work();
    return 0;
}