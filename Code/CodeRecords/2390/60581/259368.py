#include <cstdio>
#include <iostream>
#define ll long long
#define maxm 1<<13
#define il inline
ll num[15],ans;
int a[maxm],bix[15],n;
il bool check(int x,int k)
{
    for(int i=1;i<bix[k];i++) if(a[x+i]!=a[x+i-1]+1)return 0;
    return 1;
}
il void swap(int x,int y,int k)
{
    for(int i=0;i<bix[k];i++) std::swap(a[x+i],a[y+i]);
}
void dfs(int now,int k)
{
    //printf("%d %d\n",now,k);
    if(now==n+1)
    {
        ans+=num[k];
        return;
    }
    int c1=0,c2=0;
    for(int i=1;i<=bix[n];i+=bix[now])
    if(!check(i,now))
    {
        if(!c1) c1=i;
        else
        {
            if(!c2) c2=i;
            else return;
        }
    }
    if(!c1&&!c2)
     dfs(now+1,k);
    else
    {
        if(c1&&!c2)
        {
            swap(c1,c1+bix[now-1],now-1);
            dfs(now+1,k+1);
            swap(c1,c1+bix[now-1],now-1);
        }
        else
        {
            for(int x=0;x<=1;x++)
             for(int y=0;y<=1;y++)
             {
                swap(c1+x*bix[now-1],c2+y*bix[now-1],now-1);
                if(check(c1,now)&&check(c2,now))
                {
                    dfs(now+1,k+1);
                    swap(c1+x*bix[now-1],c2+y*bix[now-1],now-1);
                    break;
                }
                swap(c1+x*bix[now-1],c2+y*bix[now-1],now-1);
             }  
        }
    }
}
int main()
{
    scanf("%d",&n);
    num[0]=1;
    for(int i=1;i<=12;i++) num[i]=num[i-1]*i;
    bix[0]=1;
    for(int i=1;i<=12;i++) bix[i]=bix[i-1]<<1;
    for(int i=1;i<=bix[n];i++) scanf("%d",a+i);
    dfs(0,0);
    printf("%lld\n",ans);
    return 0;
}
