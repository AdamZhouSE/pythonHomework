#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;
struct node
{
    int pos,h;
}a[100050];
int dp[100050][2];
int cmp(node a,node b)
{
    return a.pos<b.pos;
}
int main()
{
    int n;
    while(~scanf("%d",&n))
    {
        for(int i=0;i<n;i++)
        {
            scanf("%d%d",&a[i].pos,&a[i].h);
        }
        a[n].pos=2000000600;
        sort(a,a+n,cmp);
        memset(dp,0,sizeof(dp));
        for(int i=0;i<n;i++)
        {
            if(i==0)
            {
                dp[i][0]=1;
                if(a[i].pos+a[i].h<a[i+1].pos)
                dp[i][1]=1;
            }
            else
            {
                dp[i][1]=max(dp[i-1][1],dp[i-1][0]);
                dp[i][0]=max(dp[i-1][1],dp[i-1][0]);
                if(a[i].pos+a[i].h<a[i+1].pos)
                dp[i][1]=max(dp[i][1],dp[i-1][0]+1);
                if(a[i].pos+a[i].h<a[i+1].pos)
                dp[i][1]=max(dp[i][1],dp[i-1][1]+1);
                if(a[i].pos-a[i].h>a[i-1].pos)
                dp[i][0]=max(dp[i][0],dp[i-1][0]+1);
                if(a[i].pos-a[i].h>a[i-1].pos+a[i-1].h)
                dp[i][0]=max(dp[i][0],dp[i-1][1]+1);
            }
        }
        printf("%d\n",max(dp[n-1][1],dp[n-1][0]));
    }
}