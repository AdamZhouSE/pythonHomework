#include<iostream>
#include<vector>
#include<cstdio>
#include<string>
#include<sstream>
using namespace std;
typedef long long ll;
const int maxn=10005;
vector<int> mp[maxn];
int n,m,ans,low[maxn],dfn[maxn],par[maxn],ap[maxn],cnt;
void init(){
    ans=0;
    cnt=0;
    for(int i=0;i<=n;i++){
        low[i]=dfn[i]=0;
        par[i]=0;
        ap[i]=0;
        mp[i].clear();
    }
}
void tarjan(int u){
    dfn[u]=low[u]=++cnt;  //cnt记录遍历次序
    int son=0;  //记录子树数量
    for(int i=0;i<mp[u].size();i++){
        int v=mp[u][i];
        if(!dfn[v]){ //v未被访问，(u,v)为树边
            son++;
            //记录v的父亲节点
            par[v]=u;
            tarjan(v);
            low[u]=min(low[u],low[v]);
            //根节点，子树数量大于1即为割点
            if(dfn[u]==1&&son>1&&!ap[u])
                ap[u]=1,ans++;
            //其余节点子树可追溯到最早的祖先节点要么为v要么为u
            else if(dfn[u]!=1&&low[v]>=dfn[u]&&!ap[u])
                ap[u]=1,ans++;
        }
        else if(par[v]!=u) //节点v已被访问，则(u,v)为回边
            low[u]=min(low[u],dfn[v]);
    }
}
int main(){
    int a,b;
    string s;
    while(~scanf("%d",&n)&&n){
        init();
        getchar();
        while(1){
            getline(cin,s);
            stringstream ss(s);
            ss>>a;
            if(!a)break;
            while(ss>>b&&b){
                mp[a].push_back(b);
                mp[b].push_back(a);
            }
        }
        tarjan(1);
        cout<<ans<<endl;
    }
    return 0;
}