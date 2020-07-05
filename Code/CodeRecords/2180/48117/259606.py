#include<bits/stdc++.h>FSYAKIOI
using namespace std;
typedef long long int ll;
const ll maxn=4E5+5;
ll sa[maxn],rk[maxn],y[maxn],c[maxn],n,m,height[maxn],ans,f[maxn];
string s1,s2,str;
void SS()
{
    m='~';
    for(int i=1;i<=n;++i)++c[rk[i]=str[i]];
    for(int i=1;i<=m;++i)c[i]+=c[i-1];
    for(int i=n;i>=1;--i)sa[c[rk[i]]--]=i;
    for(int k=1;k<=n;k<<=1)
    {
        int num=0;
        for(int i=n-k+1;i<=n;++i)y[++num]=i;
        for(int i=1;i<=n;++i)if(sa[i]>k)y[++num]=sa[i]-k;
        for(int i=1;i<=m;++i)c[i]=0;
        for(int i=1;i<=n;++i)++c[rk[i]];
        for(int i=1;i<=m;++i)c[i]+=c[i-1];
        for(int i=n;i>=1;--i)sa[c[rk[y[i]]]--]=y[i],y[i]=0;
        swap(rk,y);
        rk[sa[1]]=num=1;
        for(int i=2;i<=n;++i)
        {
            if(y[sa[i]]==y[sa[i-1]]&&y[sa[i]+k]==y[sa[i-1]+k])rk[sa[i]]=num;
            else rk[sa[i]]=++num;
        }
        if(num==n)break;
        m=num;
    }
}
void lcp()
{
    int cur=0;
    for(int i=1;i<=n;++i)
    {
        if(cur)--cur;
        int j=sa[rk[i]-1];
        while(str[j+cur]==str[i+cur])++cur;
        height[rk[i]]=cur;
    }
}
void out()
{
    cout<<str<<" "<<n<<endl;
    for(int i=1;i<=n;++i)cout<<sa[i]<<' ';
    cout<<endl;
    for(int i=1;i<=n;++i)cout<<height[i]<<' ';
    cout<<endl;
    for(int i=1;i<=n;++i,cout<<endl)
        for(int j=sa[i];j<=n;++j)
            cout<<str[j];
}
void solve(int flag,string PCF)
{
    memset(height,0,sizeof(height));
    memset(rk,0,sizeof(rk));
    memset(y,0,sizeof(y));
    memset(c,0,sizeof(c));
    memset(f,0,sizeof(f));
    n=PCF.size();
    PCF="~"+PCF;
    str=PCF;
    SS();
    lcp();
    stack<ll>S;
    ll sum=0;
    for(int i=2;i<=n;++i)
    {
        while(S.size()&&height[S.top()]>=height[i])S.pop();
        if(S.size()==0)f[i]=height[i]*(i-1);
        else f[i]=f[S.top()]+height[i]*(i-S.top());
        S.push(i);
        sum+=f[i]*flag;
    }
    ans+=sum;
}
int main()
{
//  freopen("a.in","r",stdin);
    ios::sync_with_stdio(false);
    cin>>s1>>s2;
    solve(1,s1+"~"+s2);
    solve(-1,s1);
    solve(-1,s2);
    cout<<ans;
    return 0;
}