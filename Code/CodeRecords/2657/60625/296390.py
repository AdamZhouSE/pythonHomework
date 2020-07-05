#include<iostream>
#include<cstdio>
#include<queue>
#include<cstring>
#include<algorithm>
using namespace std;
int RD(){
    int out = 0,flag = 1;char c = getchar();
    while(c < '0' || c >'9'){if(c == '-')flag = -1;c = getchar();}
    while(c >= '0' && c <= '9'){out = out * 10 + c - '0';c = getchar();}
    return flag * out;
    }
const int maxn = 1000019,INF = 1e9;
int num,na,nume,cnt;
int head[maxn];
struct Node{int v,nxt;}E[maxn * 2];
void add(int u,int v){
    E[++nume].nxt = head[u];
    E[nume].v = v;
    head[u] = nume;
    }
int size[maxn],wson[maxn],dep[maxn],fa[maxn],top[maxn],pos[maxn],ori[maxn];
int v[maxn];
void dfs1(int id,int F){
    size[id] = 1;
    for(int i = head[id];i;i = E[i].nxt){
        int v = E[i].v;
        if(v == F)continue;
        dep[v] = dep[id] + 1;
        fa[v] = id;
        dfs1(v,id);
        size[id] += size[v];
        if(size[v] > size[wson[id]])wson[id] = v;
        }
    }
void dfs2(int id,int TP){
    top[id] = TP;
    pos[id] = ++cnt;
    ori[cnt] = id;
    if(!wson[id])return ;
    dfs2(wson[id],TP);
    for(int i = head[id];i;i = E[i].nxt){
        int v = E[i].v;
        if(v == fa[id] || v == wson[id])continue;
        dfs2(v,v);
        }
    }
#define lid (id << 1)
#define rid (id << 1) | 1
struct sag_tree{
    int l,r,max;
    }tree[maxn << 2];
void build(int id,int l,int r){
    tree[id].l = l;
    tree[id].r = r;
    if(l == r){
        tree[id].max = 0;
        return ;
        }
    int mid = (l + r) >> 1;
    build(lid,l,mid);
    build(rid,mid + 1,r);
    tree[id].max = max(tree[lid].max,tree[rid].max);
    }
void update(int id,int val, int l,int r){
    if(tree[id].l == l && tree[id].r == r){
        tree[id].max = l;
        return ;
        }
    int mid = (tree[id].l + tree[id].r) >> 1;
    if(mid < l)update(rid,val,l,r);
    else if(mid >= r)update(lid,val,l,r);
    else update(lid,val,l,mid),update(rid,val,mid + 1,r);
    tree[id].max = max(tree[lid].max,tree[rid].max);
    }
int query(int id,int l,int r){
    if(tree[id].l == l && tree[id].r == r)return tree[id].max;
    int mid = (tree[id].l + tree[id].r) >> 1;
    if(mid < l)return query(rid,l,r);
    else if(mid >= r)return query(lid,l,r);
    else return max(query(lid,l,mid),query(rid,mid + 1,r));
    }
void Qmax(int x, int y){
    int ans = 0;
    while(top[x] != top[y]){
        if(dep[top[x]] < dep[top[y]])swap(x, y);
        ans = query(1, pos[top[x]], pos[x]);
        if(ans){
            printf("%d\n", ori[ans]);
            return ;
            }
        x = fa[top[x]];
        }
    if(dep[x] > dep[y])swap(x, y);
    ans = query(1, pos[x], pos[y]);
    printf("%d\n", ori[ans]);
    }
int main(){
    num = RD();na = RD();
    for(int i = 1;i <= num - 1;i++){
        int u = RD(),v = RD();
        add(u,v),add(v,u);
        }
    dep[1] = 1;
    dfs1(1,-1);dfs2(1,1);
    build(1,1,num);
    update(1,pos[1],pos[1],pos[1]);
    for(int i = 1;i <= na;i++){
        char cmd;cin>>cmd;
        if(cmd == 'C'){
            int x = RD();
            update(1,pos[x],pos[x],pos[x]);
            }
        else{
            int x = RD();
            Qmax(x,1);
            }
        }
    return 0;
    }