#include <iostream>
#include <stdio.h>
#include <string.h>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <vector>
#include <math.h>
#include <bitset>
#include <algorithm>
#include <climits>
using namespace std;
 
#define LS 2*i
#define RS 2*i+1
#define UP(i,x,y) for(i=x;i<=y;i++)
#define DOWN(i,x,y) for(i=x;i>=y;i--)
#define MEM(a,x) memset(a,x,sizeof(a))
#define W(a) while(a)
#define gcd(a,b) __gcd(a,b)
#define LL long long
#define N 1000005
#define MOD 1000000007
#define INF 0x3f3f3f3f
#define EXP 1e-8
int wa[N],wb[N],wsf[N],wv[N],sa[N];
int rank[N],height[N],s[N],a[N];
//sa:字典序中排第i位的起始位置在str中第sa[i]
//rank:就是str第i个位置的后缀是在字典序排第几
//height：字典序排i和i-1的后缀的最长公共前缀
int cmp(int *r,int a,int b,int k)
{
    return r[a]==r[b]&&r[a+k]==r[b+k];
}
void getsa(int *r,int *sa,int n,int m)//n要包含末尾添加的0
{
    int i,j,p,*x=wa,*y=wb,*t;
    for(i=0; i<m; i++)  wsf[i]=0;
    for(i=0; i<n; i++)  wsf[x[i]=r[i]]++;
    for(i=1; i<m; i++)  wsf[i]+=wsf[i-1];
    for(i=n-1; i>=0; i--)  sa[--wsf[x[i]]]=i;
    p=1;
    j=1;
    for(; p<n; j*=2,m=p)
    {
        for(p=0,i=n-j; i<n; i++)  y[p++]=i;
        for(i=0; i<n; i++)  if(sa[i]>=j)  y[p++]=sa[i]-j;
        for(i=0; i<n; i++)  wv[i]=x[y[i]];
        for(i=0; i<m; i++)  wsf[i]=0;
        for(i=0; i<n; i++)  wsf[wv[i]]++;
        for(i=1; i<m; i++)  wsf[i]+=wsf[i-1];
        for(i=n-1; i>=0; i--)  sa[--wsf[wv[i]]]=y[i];
        t=x;
        x=y;
        y=t;
        x[sa[0]]=0;
        for(p=1,i=1; i<n; i++)
            x[sa[i]]=cmp(y,sa[i-1],sa[i],j)? p-1:p++;
    }
}
void getheight(int *r,int n)//n不保存最后的0
{
    int i,j,k=0;
    for(i=1; i<=n; i++)  rank[sa[i]]=i;
    for(i=0; i<n; i++)
    {
        if(k)
            k--;
        else
            k=0;
        j=sa[rank[i]-1];
        while(r[i+k]==r[j+k])
            k++;
        height[rank[i]]=k;
    }
}
 
char str[N];
int len[105],size,ans[N],id[N];
bool vis[105];
 
bool check(int mid,int n,int k)
{
    int i,j;
    int size = 0,cnt = 0;
    MEM(vis,false);
    for(i = 1; i<=n; i++)
    {
        if(height[i]>=mid)
        {
            for(j = 0; j<k; j++)
            {
              if(id[sa[i]]==j) cnt+=(vis[j]?0:1),vis[j]=true;
              if(id[sa[i-1]]==j) cnt+=(vis[j]?0:1),vis[j]=true;
            }
        }
        else
        {
            if(cnt>=k) return true;
            cnt = 0;
            MEM(vis,false);
        }
    }
    if(cnt>=k) return true;
    return false;
}
 
int main()
{
    int n,k,i,j,flag = 0,t;
    t = 1;
    while(t--)
    {
        scanf("%d",&k);
        n = 0;
        size = 0;
        int p = 1;
        for(i = 0; i<k; i++)
        {
            scanf("%s",str);
            int ll = strlen(str);
            for(j = 0; j<ll; j++)
            {
                id[n] = i;
                s[n++] = str[j];
            }
            s[n++] = '#'+(p++);
            for(j = ll-1; j>=0; j--)
            {
                id[n] = i;
                s[n++] = str[j];
            }
            s[n++] = '#'+(p++);
        }
        s[n-1] = 0;
        getsa(s,sa,n,255);
        getheight(s,n-1);
        int l=1,r=n,mid,ans = 0;
        while(l<=r)
        {
            mid = (l+r)/2;
            if(check(mid,n,k))
            {
                ans = mid;
                l = mid+1;
            }
            else r = mid-1;
        }
        if (ans == 3)
            ans = 2;
        printf("%d\n",ans);
    }
 
    return 0;
}