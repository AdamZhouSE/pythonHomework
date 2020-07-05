#include<bits/stdc++.h>
using namespace std;
const int N=2000000+5;
int n,m,c;
int has[N],nxt[N];
int a[N];
int f[N];
void add(int x,int d){
    for(;x<=n;x+=x&(-x)) f[x]+=d;
}
int query(int x){
    int ret=0;
    for(;x;x-=x&(-x)) ret+=f[x];return ret;
}
struct node{
    int l,r;
    int id;
    bool friend operator <(node a,node b){
        return a.l<b.l;
    }
}q[N];
int ans[N];
int pos[N];
int main()
{
    scanf("%d%d%d",&n,&c,&m);
    for(int i=1;i<=n;i++){
        scanf("%d",&a[i]);
        has[a[i]]++;
        if(pos[a[i]])nxt[pos[a[i]]]=i;
        if(has[a[i]]==2) add(i,1);
        pos[a[i]]=i;
    }
    int l,r;
    for(int i=1;i<=m;i++){
        scanf("%d%d",&q[i].l,&q[i].r);
        q[i].id=i;
    }sort(q+1,q+m+1);
    int L=1;
    for(int i=1;i<=m;i++){
        while(L<q[i].l){
            if(nxt[L]) add(nxt[L],-1);
            if(nxt[nxt[L]]) add(nxt[nxt[L]],1);
            L++;
        }
        ans[q[i].id]=query(q[i].r)-query(q[i].l-1);
    }
    for(int i=1;i<=m;i++){
        printf("%d\n",ans[i]);
    }
    return 0;
}