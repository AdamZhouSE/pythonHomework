#include<cstdio>
#include<iostream>
#include<cmath>
#include<cstring>
#include<cstdlib>
#include<algorithm>
#include<queue>
#include<bits/stdc++.h>
using namespace std;
const int N=50002;
struct node{
    string yy;
    string s;
    int id;
}e[N];
int mx[N*4],x,y;
int n,m,a[N];
int maxx(int x,int y){
    if(e[x].s>e[y].s) return x;
    else return y;
}
void pushup(int rt)
    { mx[rt]=maxx(mx[rt*2],mx[rt*2+1]); }

void build(int l,int r,int rt){
    if(l==r) {
        mx[rt]=l;
        return ;
    }
    int m=(l+r)/2;
    build(l,m,rt*2);
    build(m+1,r,rt*2+1);
    pushup(rt);
}
int query(int L,int R,int l,int r,int rt){
    if(r<L || l>R) return 0;
    if(L<=l && R>=r) return mx[rt];
    int m=(l+r)/2,ans=0;
    if(L<=m) ans=maxx(ans,query(L,R,l,m,rt*2));
    if(R>m)  ans=maxx(ans,query(L,R,m+1,r,rt*2+1));
    return ans;
}
int main(){
    cin>>n>>m; 
    scanf("\n"); //scanf("%d %d",&n,&m);
    for(int i=1;i<=n;i++) {
        getline(cin,e[i].s);
        e[i].yy=e[i].s;
        int len=e[i].s.size();
        for(int j=0;j<len;j++){
            if(e[i].s[j]<='Z' && e[i].s[j]>='A') 
               e[i].s[j]+=('a'-'A'); 
        }
    }
        
    build(1,n,1);
    for(int i=1;i<=m;i++){
        cin>>x>>y;
        //cout<<x<<y<<endl;
        if(x==y) { cout<<e[x].yy<<endl; continue; }
        int z=query(x,y,1,n,1);
        cout<<e[z].yy<<endl;
        //cout<<e[i].s<<endl;
    }
    
    return 0;
}