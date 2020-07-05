#include<bits/stdc++.h>
using namespace std;
int n,m,sum,dep[200001],a[200001],ktot,size[200001],tpos[200001],pre[200001],head[200001],tot,f[200001][25];
struct edge{
    int to,next;
}g[1000001];
inline void made(int from,int to){
    g[++tot].to=to;g[tot].next=head[from];head[from]=tot;
}
inline int read(){
    int x=0,f=1;char ch=getchar();
    while (!isdigit(ch)){if (ch=='-') f=-1;ch=getchar();}
    while (isdigit(ch)){x=(x<<1)+(x<<3)+ch-48;ch=getchar();}
    return x*f;
}
struct Trie{
    int n,son[10000001][2],cnt=1,sum,root[200001],ct[10000001];
    void ins(int &rt,int x,int T){
        ct[++cnt]=ct[rt]+1;son[cnt][0]=son[rt][0];
        son[cnt][1]=son[rt][1];rt=cnt;
        if (T==-1) return;
        register bool y=(x>>T)&1;
        ins(son[rt][y],x,T-1);
    }
    inline void insert(int pre,int rt,int x){
        root[rt]=root[pre];
        ins(root[rt],x,30);
    }
    int QUE(int i,int j,int x,int T){//序列版
        if (T==-1) return 0;
        register bool y=(x>>T)&1;
        if (ct[son[j][1^y]]>ct[son[i][1^y]]) return ((1<<T)+QUE(son[i][1^y],son[j][1^y],x,T-1));
        else return QUE(son[i][y],son[j][y],x,T-1);
    }
    int queryxx(int i,int j,int lc,int flc,int x,int T){//树上差分版
        if (T==-1) return 0;
        register bool y=(x>>T)&1;
        if (ct[son[j][1^y]]+ct[son[i][1^y]]>ct[son[lc][1^y]]+ct[son[flc][1^y]]) return ((1<<T)+queryxx(son[i][1^y],son[j][1^y],son[lc][1^y],son[flc][1^y],x,T-1));
        else return queryxx(son[i][y],son[j][y],son[lc][y],son[flc][y],x,T-1);
    }
    int queryx(int i,int j,int lc,int flc,int x,int T){
        return queryxx(root[i],root[j],root[lc],root[flc],x,T);
    }
    inline int query(int l,int r,int x){
        return QUE(root[l-1],root[r],x,30);
    }
}tr1,tr2;
void dfs0(int u,int fa){
    dep[u]=dep[fa]+1;f[u][0]=fa;tpos[u]=++ktot;pre[ktot]=u;
    tr1.insert(fa,u,a[u]);size[u]=1;
    for (int i=1;i<=21;i++) f[u][i]=f[f[u][i-1]][i-1];
    for (int i=head[u];i;i=g[i].next){
        int v=g[i].to;
        if (v==fa) continue;
        dfs0(v,u);size[u]+=size[v];
    }
}
inline int lca(int x,int y){
    if (dep[x]<dep[y]) swap(x,y);
    for (int i=21;i>=0;i--){
        if (dep[f[x][i]]>=dep[y]) x=f[x][i];
    }
    if (x==y) return x;
    for (int i=21;i>=0;i--){
        if (f[x][i]!=f[y][i]) x=f[x][i],y=f[y][i];
    }
    return f[x][0];
}
int main(){
    n=read();m=read();
    for (int i=1;i<=n;i++) a[i]=read();
    for (int i=1;i<n;i++){
        int x=read(),y=read();
        made(x,y);made(y,x);
    }
    dfs0(1,0);
    for (int i=1;i<=n;i++){
        tr2.insert(i-1,i,a[pre[i]]);
    }
    while (m--){
        int opt=read();
        if (opt==1){
            int x=read(),y=read();
            printf("%d\n",tr2.query(tpos[x],tpos[x]+size[x]-1,y));
        }else{
            int x=read(),y=read(),z=read(),a=lca(x,y);
            printf("%d\n",tr1.queryx(x,y,a,f[a][0],z,30));
        }
    }
}