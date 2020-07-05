#include<iostream>
#include<cstring>
#include<cstdio>
#include<vector>
#define maxn 1001
using namespace std;
 
vector<int> to[maxn];
int dfn[maxn],low[maxn],tot;
int col[maxn],ind[maxn],cnt;
int stack[maxn],top;
bool instack[maxn];
int n,ans;
 
void tarjan(int u){
    dfn[u]=low[u]=++tot;
    stack[++top]=u,instack[u]=true;
    for(register int i=0;i<to[u].size();i++){
        int v=to[u][i];
        if(!dfn[v]) tarjan(v),low[u]=min(low[u],low[v]);
        else if(instack[v]) low[u]=min(low[u],dfn[v]);
    }
    if(dfn[u]==low[u]){
        int v; cnt++;
        do{ v=stack[top--],instack[v]=false; col[v]=cnt; }while(v!=u);
    }
}
 
int main(){
    scanf("%d",&n);
    for(register int i=1;i<=n;i++){
        for(register int j=1;j<=n;j++){
            int tmp; scanf("%1d",&tmp);
            if(tmp) to[i].push_back(j);
        }
    }
    for(register int i=1;i<=n;i++) if(!dfn[i]) tarjan(i);
 
    for(register int i=1;i<=n;i++){
        for(register int j=0;j<to[i].size();j++){
            int v=to[i][j];
            if(col[i]!=col[v]) ind[col[v]]++;
        }
    }
    for(register int i=1;i<=cnt;i++) if(!ind[i]) ans++;
    printf("%d\n",ans);
    return 0;
}