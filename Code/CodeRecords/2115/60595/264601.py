#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
#define sqr(x) ((x)*(x))
#define mp make_pair
#define uint unsigned
#define PI pair<int,int>
inline char gc(){
    static char buf[100000],*p1=buf,*p2=buf;
    return p1==p2&&(p2=(p1=buf)+fread(buf,1,100000,stdin),p1==p2)?EOF:*p1++;
}
#define gc getchar
inline int read(){
    int x = 0; char ch = gc(); bool positive = 1;
    for (; !isdigit(ch); ch = gc()) if (ch == '-')  positive = 0;
    for (; isdigit(ch); ch = gc())  x = x * 10 + ch - '0';
    return positive ? x : -x;
}
inline void write(int a){
    if(a<0){
        a=-a; putchar('-');
    }
    if(a>=10)write(a/10);
    putchar('0'+a%10);
}
inline void writeln(int a){
    if(a<0){
        a=-a; putchar('-');
    }
    write(a); puts("");
}
inline int rnd(int x){
    return rand()%x;
}
inline ull rnd(){
    return ((ull)rand()<<30^rand())<<4|rand()%4;
}
const int N=10005;
int n,m,V,E,flag,color[N],rd[N];
queue<int> q;
vector<int> v[N],jb;
void dfs(int p,int dq){
    if(flag)return;
    if(color[p]!=-1){if(color[p]!=dq){flag=1; puts("NO"); } return;}
    color[p]=dq; V++; E+=v[p].size();
    jb.push_back(p);
    for(unsigned i=0;i<v[p].size();i++){
        dfs(v[p][i],dq^1);
    }
}
int main(){
    int T=read();
    while(T--){
        n=read(); m=read(); flag=0; memset(color,-1,sizeof(color));
        for(int i=1;i<=n;i++)v[i].clear();
        for(int i=1;i<=m;i++){
            int s=read(),t=read();
            v[s].push_back(t); v[t].push_back(s);
        }
        for(int i=1;i<=n;i++)if(color[i]==-1){
            V=E=0; jb.clear(); dfs(i,0); if(flag)break; if(E/2>V+1){puts("NO"); flag=1; break;}
            if(E/2<=V)continue;
            for(unsigned j=0;j<jb.size();j++){
                rd[jb[j]]=v[jb[j]].size(); if(v[jb[j]].size()==1)q.push(jb[j]);
            }
            while(!q.empty()){
                int t=q.front(); q.pop();
                for(unsigned j=0;j<v[t].size();j++)if(--rd[v[t][j]]==1)q.push(v[t][j]);
            }
            int ttt=0;

            for(unsigned j=0;j<jb.size();j++)if(rd[jb[j]]==2){
                int gao=0;
                for(unsigned k=0;k<v[jb[j]].size();k++)if(rd[v[jb[j]][k]]==3)gao++;
                if(gao==2){ttt++;}
            }
            if(ttt<2){
                puts("NO"); flag=1; break;
            }
        }
        if(!flag)puts("YES");
    }
}