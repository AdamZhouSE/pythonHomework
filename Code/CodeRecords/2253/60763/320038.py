#include<cstdio>
#include<cmath>
#include<iostream>
#include<algorithm>
#define neko 50010
#define mid ((L+R)>>1)
#define midd ((LL+RR)>>1)
#define chkmin(a,b) ((a)<(b)?(a):(b))
#define chkmax(a,b) ((a)>(b)?(a):(b))
#define f(i,a,b) for(register int i=(a);i<=(b);i=-(~(i)))
using std::stable_sort;
int bl[neko],Le[neko],Re[neko],a[neko],s[neko],n,m,blk;
template<typename T>
void read(T &x)
{
    char c=getchar();T p=1;x=0;
    while(!isdigit(c)){if(c=='-')p=-1;c=getchar();}
    while(isdigit(c))
    {
        x=(x<<1)+(x<<3)+(c^'0');
        c=getchar();
    }x*=p;
}
void split()
{
    int pre=1,prei=0;Le[1]=1;
    f(i,1,n)
    {
        s[i]=a[i],bl[i]=(i-1)/blk+1;
        if(bl[i]>pre)
        {
            stable_sort(s+prei,s+i);
            pre=bl[i],prei=i;
            Le[bl[i]]=i,Re[bl[i]-1]=i-1;
        }
    }Re[bl[n]]=n,stable_sort(s+prei,s+n+1);
}
int key(int l,int r,int x)
{
    int ans=1,L,R;
    f(i,l,chkmin(r,Re[bl[l]]))if(a[i]<x)++ans;
    f(i,bl[l]+1,bl[r]-1)ans+=std::lower_bound(s+Le[i],s+Re[i]+1,x)-(s+Le[i]);
    if(bl[l]!=bl[r])f(i,chkmax(l,Le[bl[r]]),r)if(a[i]<x)++ans;
    return ans;
}
int find(int l,int r,int x)
{
    int num,anss=1,L,R,LL=1,RR=1e9;
    while(LL<=RR)
    {
        num=0;
        f(i,l,chkmin(r,bl[l]*blk))if(a[i]<=midd)++num;
        f(i,bl[l]+1,bl[r]-1)num+=std::upper_bound(s+Le[i],s+Re[i]+1,midd)-(s+Le[i]);
        if(bl[l]!=bl[r])
            f(i,chkmax(l,Le[bl[r]]),r)
                if(a[i]<=midd)++num;
        if(num>=x)anss=midd,RR=midd-1;
        else LL=midd+1;
    }return anss;
}
void update(int pos,int x)
{
    a[pos]=x;int l=Le[bl[pos]],r=Re[bl[pos]];
    f(i,l,r)s[i]=a[i];
    stable_sort(s+l,s+r+1);
}
int lower(int l,int r,int x)
{
    int ans=-2147483647,L,R;
    f(i,l,chkmin(r,Re[bl[l]]))if(a[i]<x)ans=chkmax(ans,a[i]);
    f(i,bl[l]+1,bl[r]-1)
    {
        L=Le[i],R=Re[i];
        while(L<R)
        {
            if(s[mid]>=x)R=mid;
            else L=mid+1;
        }
        if(mid==Re[i])
        {
            if(s[mid]<x)ans=chkmax(ans,s[mid]);
            else ans=chkmax(ans,s[mid-1]);
        }else if(mid!=Le[i])ans=chkmax(ans,s[mid-1]);
    }
    f(i,chkmax(l,Le[bl[r]]),r)if(a[i]<x)ans=chkmax(ans,a[i]);
    return ans;
}
int upper(int l,int r,int x)
{
    int ans=2147483647,L,R;
    f(i,l,chkmin(r,Re[bl[l]]))if(a[i]>x)ans=chkmin(ans,a[i]);
    f(i,bl[l]+1,bl[r]-1)
    {
        L=Le[i],R=Re[i];
        while(L<R)
        {
            if(s[mid]>x)R=mid;
            else L=mid+1;
        }
        if(mid==Re[i]&&s[mid]<=x)continue;
        ans=chkmin(ans,s[mid]);
    }
    f(i,chkmax(l,Le[bl[r]]),r)if(a[i]>x)ans=chkmin(ans,a[i]);
    return ans;
}
int main()
{
    int opt,x,y,k;
    scanf("%d%d",&n,&m);
    f(i,1,n)read(a[i]);if(n==1)blk=1;else blk=sqrt(n);
    split();
    f(i,1,m)
    {
        read(opt),read(x),read(y);
        if(opt==1)read(k),printf("%d\n",key(x,y,k));
        if(opt==2)read(k),printf("%d\n",find(x,y,k));
        if(opt==3)update(x,y);
        if(opt==4)read(k),printf("%d\n",lower(x,y,k));
        if(opt==5)read(k),printf("%d\n",upper(x,y,k));
    }return 0;
}