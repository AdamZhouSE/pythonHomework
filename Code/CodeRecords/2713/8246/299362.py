#include<vector>
#include<cstdio>
#include<cstring>
#include<iostream>
#define P pair<int,int> 
#ifndef Judge
#define getchar() (p1==p2&&(p2=(p1=buf)+fread(buf,1,1<<21,stdin),p1==p2)?EOF:*p1++)
#endif
using namespace std;
const int M=2e5+11;
char buf[1<<21],*p1=buf,*p2=buf;
inline int read(){
    int x=0,f=1; char c=getchar();
    for(;!isdigit(c);c=getchar()) if(c=='-') f=-1;
    for(;isdigit(c);c=getchar()) x=x*10+c-'0'; return x*f;
} char sr[1<<21],z[20];int C=-1,Z;
inline void Ot(){fwrite(sr,1,C+1,stdout),C=-1;}
void print(int x,char ch='\n'){
    if(C>1<<20)Ot(); while(z[++Z]=x%10+48,x/=10);
    while(sr[++C]=z[Z],--Z);sr[++C]=ch;
} int n,m,flag,a[M],vis[M],fir[M],las[M],lg[M];
vector<P> vec[M]; int t[M<<2],mx[M<<2],st[M][21];
#define mid (l+r>>1)
#define ls k<<1
#define rs k<<1|1
#define lson ls,l,mid
#define rson rs,mid+1,r
inline void pushup(int k,int l,int r){
    if(t[k]) mx[k]=r-l+1;
    else if(l==r) mx[k]=0;
    else mx[k]=mx[rs]+mx[ls];
} void update(int k,int l,int r,int pos,int v){
    if(r<=pos) return t[k]+=v,pushup(k,l,r);
    if(mid<pos) update(rson,pos,v);
    if(l<=pos) update(lson,pos,v); pushup(k,l,r); 
} inline int get(int l,int r){
    int len=r-l+1,k=lg[len];
    return min(st[l][k],st[r-(1<<k)+1][k]);
} int main(){ n=read(),m=read();
    for(int i=1;i<=n;++i){
        st[i][0]=a[i]=read(),las[a[i]]=i;
        if(!fir[a[i]]) fir[a[i]]=i;
    } int num=0;
    for(int i=1;i<=n;lg[i++]=num)
        if((1<<num+1)<=i) ++num;

    for(int i=1;i<=n;++i) if(!st[i][0]) st[i][0]=m+1,flag=i;
    for(int j=1;j<=lg[n];++j) for(int i=1;i+(1<<j)-1<=n;++i)
        st[i][j]=min(st[i][j-1],st[i+(1<<j-1)][j-1]);

    fir[1]=1,las[1]=n;
    if(!fir[m]){
        if(!flag) return puts("NO"),0;
        else fir[m]=las[m]=flag;
    } for(int i=1;i<=m;++i) if(fir[i]){
        vec[fir[i]].push_back(P(i,1)),
        vec[las[i]+1].push_back(P(i,-1));
        if(get(fir[i],las[i])<i) return puts("NO"),0;
    } puts("YES");
    for(int i=1;i<=n;print(mx[1],' '),++i)
        for(int j=0;j<vec[i].size();++j)
            update(1,1,m,vec[i][j].first,vec[i][j].second);
    sr[++C]='\n'; return Ot(),0;
}