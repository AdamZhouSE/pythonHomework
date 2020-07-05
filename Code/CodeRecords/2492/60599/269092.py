#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
#define N 5010
using namespace std;
int c,n,mid,ans,tmp[N];
int read()
{
    int x=0,f=1;char ch=getchar();
    while(ch<'0'||ch>'9'){if(ch=='-')f=-1;ch=getchar();}
    while(ch>='0'&&ch<='9') x=x*10+ch-'0',ch=getchar();
    return x*f;
}
struct Node
{
    int x,y;
}node[N];
int cmp(Node a,Node b){return a.x<b.x;}
int work(int l,int r)
{
    if(r-l+1<c) return false;
    int sum=0;
    for(int i=l;i<=r;i++)
     tmp[++sum]=node[i].y;
    sort(tmp+1,tmp+1+sum);
    for(int i=c;i<=sum;i++)
     if(tmp[i]-tmp[i-c+1]<=mid) return true;
    return false;
}
int pd(int x)
{
    int l=1,r;
    for(r=1;r<=n;r++)
    {
        if(node[r].x-node[l].x>x) 
        {
            if(work(l,r-1)) return true;
            while(node[r].x-node[l].x>x) l++;
        }
    }
    if(work(l,n)) return true;
    return false;
}
int main()
{
    c=read(),n=read();
    for(int i=1;i<=n;i++)
     node[i].x=read(),node[i].y=read();
    sort(node+1,node+1+n,cmp);
    int L=0,R=10000;
    while(L<=R)
    {
        mid=(L+R)>>1;
        if(pd(mid)) ans=mid+1,R=mid-1;
        else L=mid+1;
    }
    printf("%d\n",ans);
    return 0; 
}