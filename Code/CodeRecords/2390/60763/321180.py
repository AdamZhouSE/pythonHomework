#include<set>
#include<map>
#include<ctime>
#include<queue>
#include<cmath>
#include<cstdio>
#include<vector>
#include<cstring>
#include<cstdlib>
#include<iostream>
#include<algorithm>
#define ll long long
#define mod 10000007
using namespace std;
int read()
{
    int x=0,f=1;char ch=getchar();
    while(ch<'0'||ch>'9'){if(ch=='-')f=-1;ch=getchar();}
    while(ch>='0'&&ch<='9'){x=x*10+ch-'0';ch=getchar();}
    return x*f;
}
int n;
int bin[20],fac[20],a[5005];
ll ans;
bool check(int x,int k)
{
    for(int i=1;i<bin[k];i++)if(a[x+i]!=a[x+i-1]+1)return 0;
    return 1;
}
void swap(int x,int y,int k)
{
    for(int i=0;i<bin[k];i++)
        swap(a[x+i],a[y+i]);
}
void dfs(int k,int now)
{
    if(k==n+1)
    {
        ans+=fac[now];
        return;
    }
    int t1=0,t2=0;
    for(int i=1;i<=bin[n];i+=bin[k])
        if(!check(i,k))
        {
            if(!t1)t1=i;
            else if(!t2)t2=i;
            else return;
        }
    if(!t1&&!t2)dfs(k+1,now);
    else if(t1&&!t2)
    {
        swap(t1,t1+bin[k-1],k-1);
        dfs(k+1,now+1);
        swap(t1,t1+bin[k-1],k-1);
    }
    else
    {
        for(int x=0;x<=1;x++)
            for(int y=0;y<=1;y++)
            {
                swap(t1+x*bin[k-1],t2+y*bin[k-1],k-1);
                if(check(t1,k)&&check(t2,k))
                {
                    dfs(k+1,now+1);
                    swap(t1+x*bin[k-1],t2+y*bin[k-1],k-1);
                    break;
                }
                swap(t1+x*bin[k-1],t2+y*bin[k-1],k-1);
            }
    }
}
int main()
{
    bin[0]=1;for(int i=1;i<20;i++)bin[i]=bin[i-1]<<1;
    fac[0]=1;for(int i=1;i<=12;i++)fac[i]=fac[i-1]*i;
    n=read();
    for(int i=1;i<=bin[n];i++)a[i]=read();
    dfs(1,0);
    cout << ans << endl;
    return 0;
}