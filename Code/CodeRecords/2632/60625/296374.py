#include<bits/stdc++.h>
#define il inline
#define ll long long
#define RE register
#define For(i,a,b) for(RE int (i)=(a);(i)<=(b);(i)++)
#define Bor(i,a,b) for(RE int (i)=(b);(i)>=(a);(i)--)
using namespace std;
const int N=100005;
int n,m,stk[N],top,lsx[N],lsy[N];
bool vis[N];
int cnt,root,siz[N],ch[N][2],fa[N],date[N],rnd[N];
il int newnode(int v){siz[++cnt]=1,fa[cnt]=0,date[cnt]=v,rnd[cnt]=rand();return cnt;}
il void up(int rt){
    siz[rt]=siz[ch[rt][0]]+siz[ch[rt][1]]+1;
    if(ch[rt][0]) fa[ch[rt][0]]=rt;
    if(ch[rt][1]) fa[ch[rt][1]]=rt;
}
int merge(int x,int y){
    if(!x||!y) return x+y;
    if(rnd[x]<rnd[y]) {ch[x][1]=merge(ch[x][1],y),up(x);return x;}    
    else {ch[y][0]=merge(x,ch[y][0]),up(y);return y;}
}
void split(int rt,int v,int &x,int &y){
    if(!rt) {x=y=0;return;}
    if(date[rt]<=v) x=rt,split(ch[rt][1],v,ch[x][1],y),up(x);
    else y=rt,split(ch[rt][0],v,x,ch[y][0]),up(y);
}
il void ins(int v){int x=0,y=0;split(root,v,x,y);root=merge(merge(x,newnode(v)),y);}
int find(int x){return !fa[x]?x:find(fa[x]);}
int main(){
    scanf("%d%d",&n,&m);
    For(i,1,n) ins(i);
    char opt[2];
    int x,y;
    For(i,1,m){
        scanf("%s",opt);
        if(opt[0]=='D') {
            scanf("%d",&x);
            stk[++top]=x;vis[x]=1;
            split(find(x),x,lsx[top],lsy[top]);
            split(lsx[top],x-1,lsx[top],y);
            fa[lsx[top]]=0,fa[lsy[top]]=0;
        }
        else if(opt[0]=='R') merge(merge(lsx[top],stk[top]),lsy[top]),vis[stk[top--]]=0;
        else {
            scanf("%d",&x);
            if(vis[x]) {printf("0\n");continue;}
            y=siz[find(x)];
            printf("%d\n",y);    
        }
    }
    return 0;    
}