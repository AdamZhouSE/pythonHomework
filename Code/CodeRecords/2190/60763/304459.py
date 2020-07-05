#include<bits/stdc++.h>
using namespace std;
#define next Next
const int N=4e5+5;
int n,m,k,q[N],cf[N],sa[N],height[N],x[N],y[N],c[N],rk[N];
char a[N];
/*char buf[1<<21],*p1=buf,*p2=buf;
inline int gc(){return p1==p2&&(p2=(p1=buf)+fread(buf,1,1<<21,stdin),p1==p2)?EOF:*p1++;}*/
#define gc getchar
inline int read()
{
    int ret=0,f=0;char c=gc();
    while(!isdigit(c)){if(c=='-')f=1;c=gc();}
    while(isdigit(c)){ret=ret*10+c-48;c=gc();}
    if(f)return -ret;return ret;
}
void SA(int n,int m)
{
    int p;
    for(int i=0;i<=n;i++)
    {
        sa[i]=rk[i]=x[i]=y[i]=0;
    }
    for(int i=1;i<=m;i++)c[i]=0;
    for(int i=1;i<=n;i++)c[x[i]=a[i]]++;
    for(int i=1;i<=m;i++)c[i]+=c[i-1];
    for(int i=n;i;i--)sa[c[x[i]]--]=i;
    for(int i=1;i;i=i*2)
    {
        p=0;
        for(int j=n-i+1;j<=n;j++)y[++p]=j;
        for(int j=1;j<=n;j++)
            if(sa[j]>i)y[++p]=sa[j]-i;
        for(int j=1;j<=m;j++)c[j]=0;
        for(int j=1;j<=n;j++)c[x[y[j]]]++;
        for(int j=1;j<=m;j++)c[j]+=c[j-1];
        for(int j=n;j;j--)sa[c[x[y[j]]]--]=y[j];
        swap(x,y);
        x[sa[1]]=1;
        p=2;
        for(int j=2;j<=n;j++)
        {
            if(y[sa[j]]==y[sa[j-1]]&&y[sa[j]+i]==y[sa[j-1]+i])x[sa[j]]=p-1;
            else x[sa[j]]=p++;
        }
        if(p>n)return;
        m=p;
    }
}
void Height()
{
    int k=0;
    for(int i=1;i<=n;i++)rk[sa[i]]=i;
    for(int i=1;i<=n;i++)
    {
        if(rk[i]==1)continue;
        if(k)k--;
        int j=sa[rk[i]-1];
        while(i+k<=n&&j+k<=n&&a[i+k]==a[j+k])k++;
        height[rk[i]]=k;
    }
}
signed main()
{
    int T=read();
    while(T--)
    {
        memset(cf,0,sizeof(cf));
        scanf("%s",a+1);
        n=strlen(a+1);
        k=read();
        height[n+1]=0;
        SA(n,122);
        Height();
        int l=1,r=0;
        for(int i=1;i<=k;i++)
        {
            while(l<=r&&height[q[r]]>=height[i])r--;
            q[++r]=i;
        }
        for(int i=k;i<=n;i++)
        {
            if(i-q[l]+1>=k)l++;
            while(l<=r&&height[q[r]]>=height[i])r--;
            q[++r]=i;
            int R;
            if(k==1)R=n-sa[i+k-1]+1;
            else R=height[q[l]];
            int L=max(height[i-k+1],height[i+1]);
            if(L<R)
            {
                cf[L+1]++;
                cf[R+1]--;
            }
        }
        int sum=cf[0],ma=1,ans=-1;
        for(int i=1;i<=n;i++)
        {
            sum+=cf[i];
            if(sum>=ma)
            {
                ma=sum;
                ans=i;
            }
        }
        printf("%d\n",ans);
    }
    return 0;
}