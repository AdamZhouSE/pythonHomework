#include<cstdio>
#include<iostream>
#include<cstring>
#include<algorithm>
#include<cmath>
#include<vector>
#include<queue>
#define N 100003
#define inf 0x3f3f3f3f
#define ll long long
using namespace std;

vector<int> adj[N];
int n,m,r,p,cnt;
int son[N],depth[N],fa[N],size[N];
int id[N],top[N],w[N];
ll c1[N],c2[N];

//以下为树状数组
inline int lowbit(int x){
    return x&(-x);
}

inline void add(int l,int r,int x){
    x %= p;
    int ad1 = (ll)(l-1)*x%p;
    int ad2 = (ll)r*x%p;
    for(int t=l;t<=n;t+=lowbit(t)){
        c1[t] = (c1[t]+x)%p;
        c2[t] = (c2[t]+ad1)%p;
    }
    for(int t=r+1;t<=n;t+=lowbit(t)){
        c1[t] = (c1[t]-x)%p;
        c1[t] = (c1[t]+p)%p;
        c2[t] = (c2[t]-ad2)%p;
        c2[t] = (c2[t]+p)%p;
    }
}

inline int qwq(int i){ //qwq
    int res = 0;
    for(int t=i;t>0;t-=lowbit(t)){
        res = (res+(ll)i*c1[t]%p)%p;
        res = (res-c2[t])%p;
        res = (res+p)%p;
    }
    return res;
}

inline int query(int l,int r){
    int res = (qwq(r)-qwq(l-1))%p;
    return (res+p)%p;
}
//以上树状数组

inline void read(int &x){
    x = 0;
    char c = getchar();
    while(c<'0'||c>'9') c = getchar();
    while(c>='0'&&c<='9'){
        x = (x<<3)+(x<<1)+(c^48);
        c = getchar();
    }
}

void print(int x){
    if(x>9) print(x/10);
    putchar(x%10+'0');
}

void dfs1(int u,int f){
    fa[u] = f;
    size[u] = 1;
    depth[u] = depth[f]+1;
    int v,t = -1,l = adj[u].size();
    for(int i=0;i<l;++i){
        v = adj[u][i];
        if(v==f) continue;
        dfs1(v,u);
        size[u] += size[v];
        if(size[v]>t){
            t = size[v];
            son[u] = v;
        }
    }
}

void dfs2(int u,int f){
    top[u] = f;
    id[u] = ++cnt;
    if(w[u]!=0)
        add(id[u],id[u],w[u]);
    if(son[u]==0) return;
    dfs2(son[u],f);
    int v,l = adj[u].size();
    for(int i=0;i<l;++i){
        v = adj[u][i];
        if(v==son[u]||v==fa[u]) continue;
        dfs2(v,v);
    }
}

int queryPath(int u,int v){
    int res = 0;
    while(top[u]!=top[v]){
        if(depth[top[u]]<depth[top[v]])
            swap(u,v);
        res = (res+query(id[top[u]],id[u]))%p;
        u = fa[top[u]];
    }
    if(depth[u]>depth[v]) swap(u,v);
    res = (res+query(id[u],id[v]))%p;
    return res;
}

void addPath(int u,int v,int k){
    k %= p;
    while(top[u]!=top[v]){
        if(depth[top[u]]<depth[top[v]])
            swap(u,v);
        add(id[top[u]],id[u],k);    
        u = fa[top[u]];
    }
    if(depth[u]>depth[v]) swap(u,v);
    add(id[u],id[v],k);
}

int querySon(int u){
    return query(id[u],id[u]+size[u]-1);
}

void addSon(int u,int k){
    k %= p;
    add(id[u],id[u]+size[u]-1,k);
}

int main(){
    int u,v;
    read(n),read(m),read(r),read(p);
    for(int i=1;i<=n;++i)
        read(w[i]);
    for(int i=1;i<n;++i){
        read(u),read(v);
        adj[u].push_back(v);
        adj[v].push_back(u);
    }    
    dfs1(r,0);
    dfs2(r,r);
    int ans,op,x,y,z;
    while(m--){
        read(op),read(x);
        if(op==1){
            read(y),read(z);
            addPath(x,y,z);
            continue;
        }
        if(op==2){
            read(y);
            ans = queryPath(x,y);
            print(ans);
            putchar('\n');
            continue;
        }
        if(op==3){
            read(z);
            addSon(x,z);
            continue;
        }
        ans = querySon(x);
        print(ans);
        putchar('\n');
    }
    return 0;
}
