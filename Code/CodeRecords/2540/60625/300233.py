#include<cstdio>
#include<algorithm>
#include<iostream>
#include<cstring>
using namespace std;
#define FOR(i,x,y) for(int i=(x);i<(y);i++)
#define M 50000
#define N 10000
//复杂度 50000*log(10000); 
struct node{
    int si,ti,mi;
    bool operator <(const node &s)const{
        return ti<s.ti;
    }
}cow[M];
struct Segment{
    struct leave{
        int l,r,mx,add;
    }tree[N<<2];
    void up(int p){
        tree[p].mx=max(tree[p<<1].mx,tree[p<<1|1].mx);
    }
    void down(int p){
        if(tree[p].add==0)return;
        tree[p<<1].add+=tree[p].add;
        tree[p<<1].mx+=tree[p].add;
        tree[p<<1|1].add+=tree[p].add;
        tree[p<<1|1].mx+=tree[p].add;
        tree[p].add=0;
    }
    void build(int l,int r,int p){
        tree[p].l=l,tree[p].r=r,tree[p].mx=0,tree[p].add=0;
        if(l==r)return;
        int mid=(l+r)>>1;
        build(l,mid,p<<1);
        build(mid+1,r,p<<1|1);
        up(p);
    }
    void update(int l,int r,int a,int p){
        if(tree[p].l==l&&tree[p].r==r){
            tree[p].add+=a;
            tree[p].mx+=a;
            return;
        }
        down(p);
        int mid=(tree[p].l+tree[p].r)>>1;
        if(mid>=r)update(l,r,a,p<<1);
        else if(mid<l)update(l,r,a,p<<1|1);
        else {
            update(l,mid,a,p<<1);
            update(mid+1,r,a,p<<1|1);
        }
        up(p);
    }
    int query(int l,int r,int p){
        if(tree[p].l==l&&tree[p].r==r){
            return tree[p].mx;
        }
        down(p);
        int mid=(tree[p].l+tree[p].r)>>1;
        if(mid>=r)return query(l,r,p<<1);
        else if(mid<l)return query(l,r,p<<1|1);
        else return max(query(l,mid,p<<1),query(mid+1,r,p<<1|1));
    }
}Tree;
int main(){
    int k,n,c,ans=0;
    cin>>k>>n>>c;
    FOR(i,0,k)scanf("%d%d%d",&cow[i].si,&cow[i].ti,&cow[i].mi);
    sort(cow,cow+k);
    Tree.build(1,n,1);
    FOR(i,0,k){
        int mx=Tree.query(cow[i].si,cow[i].ti,1);
        mx=max(c-mx,0);
        mx=min(mx,cow[i].mi);
        if(mx)Tree.update(cow[i].si,cow[i].ti-1,mx,1);
        ans+=mx;
    }
    printf("%d\n",ans);
    return 0;
}