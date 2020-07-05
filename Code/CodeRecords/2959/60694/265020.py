// https://www.luogu.com.cn/problemnew/solution/P3181
// 前缀后缀，单调栈， 同样看不懂

#include <iostream>
#include <cstring>
#include <cstdio>
#define MX 823123

using namespace std;
typedef long long ll;
typedef struct tSA
{
    int str[MX],n,m;
    int rank[MX],SA[MX],het[MX];
    int buk[MX],yp[MX];
    bool cmp(int *f,int x,int y,int w){return f[x]==f[y]&&f[x+w]==f[y+w];}
    void jsort()
    {
        for(int i=0;i<=m;i++)buk[i]=0;
        for(int i=1;i<=n;i++)buk[rank[yp[i]]]++;
        for(int i=1;i<=m;i++)buk[i]+=buk[i-1];
        for(int i=n;i>=1;i--)SA[buk[rank[yp[i]]]--]=yp[i];
    }
    void getSA()
    {
        for(int i=1;i<=n;i++)rank[i]=str[i],yp[i]=i;
        m=28;jsort();
        for(int w=1;w<n;w<<=1)
        {
            int p=0;
            for(int i=n-w+1;i<=n;i++)yp[++p]=i;
            for(int i=1;i<=n;i++)if(SA[i]>w)yp[++p]=SA[i]-w;
            jsort(),swap(rank,yp),rank[SA[1]]=p=1;
            for(int i=2;i<=n;i++)rank[SA[i]]=(cmp(yp,SA[i],SA[i-1],w)?p:++p);
            m=p;
        }
        int k=0;
        for(int i=1;i<=n;i++)
        {
            k=(k?k-1:0);
            while(str[i+k]==str[SA[rank[i]-1]+k])k++;
            het[rank[i]]=k;
        }
    }
}SA;
SA sa;
char str[MX];
int l1,l2,top,sum[MX];
pair<int,ll>stk[MX];
void work()
{
    ll ans=0;
    stk[0]=make_pair(1,0);
    for(int i=1;i<=sa.n;i++)sum[i]=sum[i-1]+(sa.SA[i]<=l1);
    for(int i=1;i<=sa.n;i++)
    {
        while(top&&sa.het[stk[top].first]>sa.het[i])top--;
        top++;
        stk[top]=make_pair(i,(sum[i-1]-sum[stk[top-1].first-1])*sa.het[i]+stk[top-1].second);
        if(sa.SA[i]>l1+1)ans+=stk[top].second;
    }
    top=0;
    for(int i=1;i<=sa.n;i++)sum[i]=sum[i-1]+(sa.SA[i]>l1+1);
    for(int i=1;i<=sa.n;i++)
    {
        while(top&&sa.het[stk[top].first]>sa.het[i])top--;
        top++;
        stk[top]=make_pair(i,(sum[i-1]-sum[stk[top-1].first-1])*sa.het[i]+stk[top-1].second);
        if(sa.SA[i]<=l1)ans+=stk[top].second;
    }
    printf("%lld\n",ans);
}
int main()
{
    scanf("%s",str+1);l1=strlen(str+1);
    scanf("%s",str+l1+2);
    str[l1+1]='z'+1;
    sa.n=strlen(str+1);
    for(int i=1;i<=sa.n;i++)sa.str[i]=str[i]-'a'+1;
    sa.getSA();
    work();
    return 0;
}