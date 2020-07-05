#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <map>
using namespace std;
namespace IStream{const int LLL=1<<15;char buffer[LLL],*SSS,*TTT;char Get_Char(){if(SSS==TTT){TTT=(SSS=buffer)+fread(buffer,1,LLL,stdin);if(SSS==TTT) return EOF;}return *SSS++;}int Getint(){char c;int re=0,f=1;for(c=Get_Char();c<'0'||c>'9';c=Get_Char())if(c=='-')f=-1;while(c>='0'&&c<='9')re=(re<<1)+(re<<3)+(c-'0'),c=Get_Char();return re*f;}}class OStream{private:static const int LLL=1<<15;char staack[21];int topp;char buffer[LLL],*SSS;public:OStream(){SSS=buffer;}void Putint(int x,int flag){bool fl=false;if(flag==1) staack[++topp]=' ';if(flag==2) staack[++topp]='\n';if(x<0) x=-x,fl=true;if(!x) staack[++topp]='0';while(x)staack[++topp]=x%10+'0',x/=10;if(fl)staack[++topp]='-';while(topp){if(SSS==buffer+LLL-1){fwrite(buffer,1,SSS-buffer,stdout);SSS=buffer;}*SSS++=staack[topp--];}}~OStream(){fwrite(buffer,1,SSS-buffer,stdout);*SSS=0;}}os;
#ifndef ONLINE_JUDGE
inline int Getint(){int x=0,f=1;char ch=getchar();while('0'>ch||ch>'9'){if(ch=='-')f=-1;ch=getchar();}while('0'<=ch&&ch<='9'){x=x*10+ch-'0';ch=getchar();}return x*f;}
#else
using namespace IStream;//这上面是从PoPoQQQ那儿学来的输入输出，比一般的Getint还是要快些
#endif
struct Seg{
    int x,h,flag;
}w[80005];
bool cmp(Seg a,Seg b){
    return a.x<b.x;
}
map<int,int>Map;
int cnt=0,mk[40005];
struct node{
    int L,r,Sum;
}Tree[160005];
void Build(int v,int L,int r){
    Tree[v]=(node){L,r,0};
    if(L==r)return;
    Build(2*v,L,(L+r)/2);
    Build(2*v+1,(L+r)/2+1,r);
}
struct NODe{
    int vl,pos,hh;
}h[40005];
bool cmp2(NODe a,NODe b){
    return a.vl<b.vl;
}
bool cmpcmp(NODe a,NODe b){
    return a.pos<b.pos;
}
void Insert(int v,int pos,int vl){
    Tree[v].Sum+=vl;
    if(Tree[v].L==Tree[v].r)return;
    else Insert(2*v+(pos>Tree[2*v].r),pos,vl);
}
long long Ask(int v){
    if(Tree[v].L==Tree[v].r)return mk[Tree[v].L];
    if(Tree[2*v+1].Sum)return Ask(2*v+1);
    return Ask(2*v);
}
int LL[40005],rr[40005];
int main(){
    int n=Getint();
    for(int i=1;i<=n;i++){//很少写离散化，所以离散化的部分代码很丑（其实整个代码都很丑）
        LL[i]=Getint(),rr[i]=Getint();
        h[i]=(NODe){Getint(),i};
    }
    sort(h+1,h+n+1,cmp2);
    for(int i=1;i<=n;i++)
        h[i].hh=h[i-1].hh+(h[i-1].vl!=h[i].vl),mk[h[i].hh]=h[i].vl;
    cnt=h[n].hh;
    sort(h+1,h+n+1,cmpcmp);
    for(int i=1;i<=n;i++){
        w[2*i-1]=(Seg){LL[i],h[i].hh,1};
        w[2*i]=(Seg){rr[i],h[i].hh,-1};
    }
    sort(w+1,w+2*n+1,cmp);
    long long Area=0;
    Build(1,0,cnt);
    for(int i=1;i<=2*n;i++){
        Area+=Ask(1)*(long long)(w[i].x-w[i-1].x);
        Insert(1,w[i].h,w[i].flag);
    }
    cout<<Area<<"\n";
    return 0;
}
