#include<cstdio>
#include<algorithm>
using namespace std;
const int maxn=3e5+10;
int n,k,sz,ts;
int a,b,c;
int s[maxn],hs[maxn],tt[maxn];
struct tree{int s,mid,lp,rp;}t[maxn*25];
void build(int l,int r,int k){
    t[k].mid=l+r>>1;
    if(l==r) return;
    t[k].lp=++ts,t[k].rp=++ts;
    build(l,t[k].mid,t[k].lp);
    build(t[k].mid+1,r,t[k].rp);
}
void put(int l,int r,int k,int nk,int p){
    t[nk]=(tree){t[k].s+1,t[k].mid};
    if(l==r) return;
    if(p<=t[nk].mid){
        t[nk].lp=++ts,t[nk].rp=t[k].rp;
        put(l,t[nk].mid,t[k].lp,t[nk].lp,p);
    }
    else{
        t[nk].rp=++ts,t[nk].lp=t[k].lp;
        put(t[nk].mid+1,r,t[k].rp,t[nk].rp,p);
    }
}
int search(int k,int nk,int v){
    if((t[k].lp==0)&&(t[k].rp==0)) return t[k].mid;
    int w=t[t[nk].lp].s-t[t[k].lp].s;
    if(v<=w) return search(t[k].lp,t[nk].lp,v);
    else return search(t[k].rp,t[nk].rp,v-w);
}
int main(){
    scanf("%d%d",&n,&k);
    for(int i=1;i<=n;i++){
        scanf("%d",&s[i]);
        hs[i]=s[i];
    }
    sort(hs+1,hs+n+1);
    sz=unique(hs+1,hs+n+1)-hs-1;
    build(1,sz,tt[0]);
    for(int i=1;i<=n;i++){
        int pos=lower_bound(hs+1,hs+sz+1,s[i])-hs;
        tt[i]=++ts;
        put(1,sz,tt[i-1],tt[i],pos);
    }
    for(int i=1;i<=k;i++){
        scanf("%d%d%d",&a,&b,&c);
        printf("%d\n",hs[search(tt[a-1],tt[b],c)]);
    }
    return 0;
}