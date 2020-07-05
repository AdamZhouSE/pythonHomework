#include <bits/stdc++.h>
#define I inline
using namespace std;
const int N=2e5+5;char s[N];
int n,lst=1,sz=1,w[N],ans,hd[N],V[N];
int nx[N],t,tt,T[N],ch[N*20][2];
struct SAM{
    int link,len;
    map<int,int>nx;
}a[N];
I void build(int x){
    int p=lst,np=++sz;
    a[np].len=a[p].len+1;
    while(p && !a[p].nx.count(x))
        a[p].nx[x]=np,p=a[p].link;
    if (!p) a[np].link=1;
    else{
        int q=a[p].nx[x];
        if (a[q].len==a[p].len+1)
            a[np].link=q;
        else{
            int nq=++sz;a[nq]=a[q];
            a[nq].len=a[p].len+1;
            a[np].link=a[q].link=nq;
            while(p && a[p].nx[x]==q)
                a[p].nx[x]=nq,p=a[p].link;
        }
    }
    lst=np;
}
I void add(int u,int v){V[++t]=v;nx[t]=hd[u];hd[u]=t;}
I void ins(int &x,int v,int d){
    if (!x) x=++tt;
    if (~d) ins(ch[x][(v>>d)&1],v,d-1);
}
I int query(int x,int y,int d){
    if (!~d) return 0;
    if (ch[x][0] && ch[x][1]){
        if (ch[y][0] && ch[y][1])
            return max(query(ch[x][0],ch[y][1],d-1),query(ch[x][1],ch[y][0],d-1))|(1<<d);
        else{
            bool v=ch[y][1];
            return query(ch[x][v^1],ch[y][v],d-1)|(1<<d);
        }
    }
    else{
        bool v=ch[x][1];
        return ch[y][v^1]?(query(ch[x][v],ch[y][v^1],d-1)|(1<<d)):query(ch[x][v],ch[y][v],d-1);
    }
}
I int merge(int x,int y){
    if (!x || !y) return x|y;int z=++tt;
    ch[z][0]=merge(ch[x][0],ch[y][0]);
    ch[z][1]=merge(ch[x][1],ch[y][1]);
    return z;
}
I void dfs(int x){
    for (int v,i=hd[x];i;i=nx[i]){
        dfs(v=V[i]);
        if (T[x] && T[v])
            ans=max(ans,a[x].len+query(T[x],T[v],18));
        T[x]=merge(T[x],T[v]);
    }
}
int main(){
    scanf("%d%s",&n,s+1);
    for (int i=1;i<=n;i++) scanf("%d",&w[i]);
    for (int i=n;i;i--) build(s[i]),ins(T[lst],w[i],18);
    for (int i=2;i<=sz;i++) add(a[i].link,i);dfs(1);
    return printf("%d\n",ans),0;
}