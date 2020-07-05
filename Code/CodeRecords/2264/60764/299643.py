#include<iostream>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<stack>
#include<cstdio>
#include<queue>
#include<map>
#include<vector>
#include<set>
using namespace std;
const int maxn=510;
const int INF=0x3fffffff;
typedef long long LL;
//最后得到点双连通分量
//还要求不同的方案数
 
//用Tarjan跑出割点，然后DFS搜索所有的联通快
//计算每一个联通快中的割点数目
//分类讨论：
//如果没有割点
//至少需要建立两个出口
//从任意非割点的地方选择两个点建立
//如果这个分组只有一个割点
//只需要在分组内设立一个出口
//可以设立在任意一个非割点的地方
//如果有两个及以上个割点，则无需建立，可以直接到达其他联通块
//https://www.luogu.com.cn/problemnew/solution/P3225
int dfn[maxn],vis[maxn],low[maxn];
bool cut[maxn]; //是不是割点
int head[maxn];
LL ans,cnt,dfnn,ans1,ans2,group,cases,root,rs,cuts;
int n,m;
void inti(){
    memset(head,-1,sizeof(head));
    memset(dfn,0,sizeof(dfn));
    memset(low,0,sizeof(low));
    memset(cut,0,sizeof(cut));
    memset(vis,0,sizeof(vis));
    dfnn=0;  //至少需要的出口数
    cnt=0;ans1=0;group=0;
    ans2=1; //方案数
}
struct edge{
    int to,next;
}e[maxn*maxn];
int num=0;
void add(int u,int v){
    e[num]=edge{v,head[u]};
    head[u]=num++;
}
void tarjin(int u,int fa){   //得到所有的割点
    int v;
    low[u]=dfn[u]=++dfnn;
    for(int i=head[u];i!=-1;i=e[i].next){
        v=e[i].to;
        if(!dfn[v]){
            tarjin(v,u);
            low[u]=min(low[u],low[v]);
            if(low[v]>=dfn[u]){  //割点
                if(u!=root){ ////如果u不是子树的根节点
                    cut[u]=1; 
                }
                else rs++; //根节点子节点数增加 
            }
        }
        else if(v!=fa){  //如果v不是u的父节点，但是v已经访问过
            low[u]=min(low[u],dfn[v]);   //判断是否能够更新Low
        }
    }
}
void dfs(int u){//DFS搜索一边联通块   ,得到这个连通块中的割点数
    int v;
    vis[u]=group;
    ans++; //非割点数
    for(int i=head[u];i!=-1;i=e[i].next){
        v=e[i].to;
        if(cut[v]&&vis[v]!=group){  ////如果v是割点并且v没有在这个分组内被访问过
            cuts++; //割点数增加
            vis[v]=group;
        }
        if(!vis[v]){
            dfs(v);
        }
    }
}
int main(){
    LL u,v;
    cases=1;
    while(cin>>m&&m){
        inti();
        n=-1;
        for(int i=1;i<=m;i++){
            cin>>u>>v;
            add(u,v);add(v,u);
            if(max(u,v)>n) n=max(u,v);
        }
        for(int i=1;i<=n;i++){
            if(!dfn[i]){
                root=i;
                rs=0;
                tarjin(i,i);
                if(rs>=2) cut[i]=1; ////如果子树根节点的儿子数不少于2个，则这个根节点才是割点
            }
        }
        for(int i=1;i<=n;i++){  ////枚举所有点来搜索分组
            if(!vis[i]&&!cut[i]){
                ++group;
                ans=0;cuts=0;
                dfs(i);
                if(cuts==0){ //如果这个连通块没有割点，就是两个出口
                    ans1+=2;
                    ans2*=(ans)*(ans-1)/2;
                }
                else if(cuts==1){  //如果有一个割点
                    ans1+=1;
                    ans2*=ans;//可以设立在任意一个非割点的地方
                }
                //如果有两个及以上个割点，则无需建立，可以直接到达其他联通块
            }
        }
        cout<<"Case "<<cases++<<": "<<ans1<<" "<<ans2<<endl;
    }
return 0;
}