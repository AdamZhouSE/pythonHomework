#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<string>
#include<cmath>
#include<algorithm>
using namespace std;
inline int rd(){
    int x=0,f=1;
    char ch=getchar();
    for(;!isdigit(ch);ch=getchar()) if(ch=='-') f=-1;
    for(;isdigit(ch);ch=getchar()) x=x*10+ch-'0';
    return x*f;
}
inline void write(int x){
    if(x<0) putchar('-'),x=-x;
    if(x>9) write(x/10);
    putchar(x%10+'0');
    return ;
}
int n,m;
int head[1000006],nxt[1000006],to[1000006];
int v[1000006];
int total=0;
void add(int x,int y){
    total++;
    to[total]=y;
    nxt[total]=head[x];
    head[x]=total;
    return ;
}
int dfn[1000006],low[1000006];
int tot=0;
int book[1000006];
int set=0;
int sta[1000006];
int color[1000006];
int cnt=0;
int v2[1000006];
int f[100006];
void tarjan(int x,int fa){
    low[x]=dfn[x]=++tot;
    sta[++set]=x;
    f[x]=fa;
    book[x]=1;
    for(int e=head[x];e;e=nxt[e]){
        if(to[e]==fa) continue;
        if(!dfn[to[e]]){
            tarjan(to[e],x);
            low[x]=min(low[x],low[to[e]]);
        }
        else if(book[to[e]]) low[x]=min(low[x],dfn[to[e]]);
    }
    if(dfn[x]==low[x]){
        book[x]=0;
        cnt++;
        color[x]=cnt;
        v2[cnt]=v[x];
        while(set&&sta[set]!=x){
            int h=sta[set];
            book[h]=0;
            color[h]=cnt;
            v2[cnt]+=v[h];
            set--;
        }
        set--;
    }
    return ;
}
int du[100006];
int main(){
    n=rd(),m=rd();
    for(int i=1;i<=m;i++){
        int x=rd(),y=rd();
        add(x,y),add(y,x);
    }
    for(int i=1;i<=n;i++) if(!dfn[i]) tarjan(i,i);
    for(int i=1;i<=n;i++) if(color[i]!=color[f[i]]) du[color[i]]++,du[color[f[i]]]++;
    int ans=0;
    for(int i=1;i<=cnt;i++) if(du[i]==1) ans++;
    write((ans+1)/2);
    cout<<'\n';
    return 0;
}