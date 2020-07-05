#include<bits/stdc++.h>
using namespace std;
const int mod=1e9+7;
typedef long long ll;
typedef pair<int,int> pii;
int key[30],maxl,fr[30],ans=1,las,pre[10100],n;
string s;
vector<string>buc[233];
ll seed;
string S[10010];
int rnd()
{
    ll ret=seed;
    seed=(seed*7+13)%mod;
    return ret%mod;
}
unordered_map<int,pii>f;
#define mp(x,y) make_pair(x,y)
void print(int x)
{
    if(pre[x])print(pre[x]);
    cout<<S[x]<<endl;   
}
int main()
{
    seed=19260817;
    for(int i=0;i<26;++i)key[i]=rnd();
    while(cin>>s)
    {
        int l=s.length();
        buc[l].push_back(s);
        if(l>maxl)maxl=l;
    }
    for(int l=1;l<=maxl;++l)
    {
        if(buc[l].empty())continue;
        for(int i=0,p=buc[l].size();i<p;++i)
        {
            int has=0;
            s=buc[l][i];S[++n]=s;
            for(int j=0;j<26;++j)fr[j]=0;
            for(int j=0;j<l;++j)++fr[s[j]-'a'],has=(has+key[s[j]-'a'])%mod;
            f[has].first=1,f[has].second=n;
            for(int j=0;j<26;++j)
            {
                int pp=(has-key[j]+mod)%mod;
                if(f.count(pp)&&f[pp].first+1>f[has].first)f[has].first=f[pp].first+1,pre[n]=f[pp].second;
            }
            if(f[has].first>=ans)las=n,ans=f[has].first;
        }
    }
    printf("%d\n",ans);
    print(las);
}