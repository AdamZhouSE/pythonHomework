#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
#define maxn 100010
inline int read();
struct edge{
    int next;
    int to;
    int w;
}e[maxn*3];
int pre[maxn],dep[maxn],son[maxn],fa[maxn],siz[maxn],top[maxn],XOR[maxn],_XOR[maxn];
int cnt=1;
namespace lys{
    int n,m;
    void add(int x,int y,int w){
        e[cnt].to=y;e[cnt].next=pre[x];e[cnt].w=w;pre[x]=cnt++;
        e[cnt].to=x;e[cnt].next=pre[y];e[cnt].w=w;pre[y]=cnt++;
    }
    void dfs1(int node,int deep){
        dep[node]=deep;
        siz[node]=1;
        int i,v;
        for(i=pre[node];~i;i=e[i].next){
            v=e[i].to;
            if(v==fa[node]) continue ;
            fa[v]=node;
            dfs1(v,deep+1);
            if(siz[son[node]]<siz[v])
                son[node]=v;
        }
    }
    void dfs2(int node,int tp){
        top[node]=tp;
        if(!son[node]) return ;
        int i,v;
        for(i=pre[node];~i;i=e[i].next){
            v=e[i].to;
            if(v==fa[node]) continue ;
            if(v==son[node]){
                XOR[son[node]]=XOR[node]^e[i].w;
                dfs2(son[node],tp);
            }
            else{
                _XOR[v]=e[i].w;
                dfs2(v,v);
            }
        }
    }
    int work(int x,int y){
        int res=0;
        while(true){
            if(top[x]==top[y]){
                res^=XOR[x]^XOR[y];
                return res;
            }
            if(top[x]>=top[y]){
                res^=XOR[x]^_XOR[top[x]];
                x=fa[top[x]];
            }
            else{
                res^=XOR[y]^_XOR[top[y]];
                y=fa[top[y]];
            }
        }
    }
    int main(){
        n=read();
        int i,x,y,w;
        memset(pre,-1,sizeof pre);
        for(i=1;i<n;i++){
            x=read(); y=read(); w=read();
            add(x,y,w);
        }
        dfs1(1,0);
        dfs2(1,1);
        //for(i=1;i<=n;i++) cout<<XOR[i]<<endl;
        //for(i=1;i<cnt;i++) cout<<e[i].w<<endl;
        m=read();
        for(i=1;i<=m;i++){
            x=read(); y=read();
            printf("%d\n",work(x,y));
        }
        return 0;
    }
}
int main(){
    lys::main();
    return 0;
}
inline int read(){
    int k=0,f=1;
    char c=getchar();
    while(c<'0'||c>'9'){
        if(c=='-')
            f=-1;
        c=getchar();
    }
    while(c>='0'&&c<='9'){
        k=k*10+c-'0';
        c=getchar();
    }
    return k*f;
}