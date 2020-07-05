#include<iostream>
#include<cstring>
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<string>
#include<algorithm>
#include<stack>
#define ms(a) memset(a,0,sizeof(a))
using namespace std;
const int MAXN=1010;
const int MAXM=1000010;
int head[MAXN],next[MAXM],ver[MAXM],indexx=0;
int dfn[MAXN],low[MAXN],belong[MAXN],cnt=0;
int indegree[MAXN],xxx[MAXM];
int father[MAXN],sign[MAXN];
bool vis[MAXN]={0};
int tot=0; 
int k=0;
int counts=0;
int n,m;
stack<int>s;
inline void add(int x,int y)
{
    ver[indexx]=y;
    xxx[indexx]=x;
    next[indexx]=head[x];
    head[x]=indexx;
    sign[indexx]=counts;
}
void tarjan(int x)
{
    dfn[x]=low[x]=++tot;
    s.push(x);
    vis[x]=true;
    for(int i=head[x];i;i=next[i]){
        int y=ver[i];
        if(sign[i]==father[x]) continue;
            if(dfn[y]==0){
                father[y]=sign[i];
                tarjan(y);
                low[x]=min(low[x],low[y]);
            }
            else if(vis[y]&&low[x]>dfn[y]){ 
                low[x]=dfn[y];
            }
        
    }
    if(dfn[x]==low[x]){
        cnt++;
        while(1){
            int xx=s.top();
            belong[xx]=cnt;
            vis[xx]=false;
            s.pop();
            if(xx==x)break;
        }
        vis[x]=false;
        belong[x]=cnt;
    }
    return ;
}
int main()
{
    //freopen("3.in","r",stdin);
    //freopen("3.out","w",stdout);
    scanf("%d%d",&n,&m);
    for(int i=1;i<=m;i++){
        int x,y;
        scanf("%d%d",&x,&y);
        counts++;indexx++;add(x,y);indexx++;add(y,x);
        father[x]=y;father[y]=x;
    }
    memset(vis,false,sizeof(vis));
    for(int i=1;i<=n;i++){
        if(!belong[i]) tarjan(i);
    }
    ms(indegree);
    for(int i=1;i<=indexx;i=i+2){
        int x=belong[xxx[i]];
        int y=belong[ver[i]];
        if(x==y)continue;
        indegree[x]++;
        indegree[y]++;
    }int k=0;
    for(int i=1;i<=cnt;i++){
        if(indegree[i]==1)k++;
    }
    printf("%d",(k+1)/2);
    puts("");
    //fclose(stdin);
    //fclose(stdout);
    return 0;
}



