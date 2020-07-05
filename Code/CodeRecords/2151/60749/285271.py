#include<bits/stdc++.h>
using namespace std;
const int mod=1e9+7;
const int N=305;
const int M=1e5+5;
const int Inv2=(mod+1)>>1;
int n,m,ans;
int U[M],V[M],W[M],Pow[15];
struct data{ int x,y; } b[3],a[N][N],res[3],w[3],E[3][3],Uni={1,0},Inv3;
inline int Plus(int a, int b){ a+=b; return a-(a>=mod?mod:0); }
inline int Minus(int a, int b){ a-=b; return a<0?a+mod:a; }
data operator + (const data& a, const data& b){ return (data){Plus(a.x,b.x),Plus(a.y,b.y)}; }
data operator - (const data& a, const data& b){ return (data){Minus(a.x,b.x),Minus(a.y,b.y)}; }
data operator * (const data& a, const data& b){ return (data){(1ll*a.x*b.x%mod+mod-3ll*a.y*b.y%mod)%mod,(1ll*a.x*b.y+1ll*a.y*b.x)%mod}; }
inline int fastpow(int x, int y){ int res=1; for (; y; y>>=1,x=1ll*x*x%mod) if (y&1) res=1ll*res*x%mod; return res; }
inline data Inv(data a){
    int res=fastpow((1ll*a.x*a.x%mod+3ll*a.y*a.y%mod)%mod,mod-2);
    return (data){1ll*res*a.x%mod,1ll*res*(mod-a.y)%mod};
}
inline data DET(){
    int rev=0; data cur=(data){1,0};
    for (int i=1; i<n; i++){
        int p=i;
        for (; p<n && !a[p][i].x && !a[p][i].y; p++);
        if (p>=n) return (data){0,0};
        if (i!=p){ rev^=1; for (int j=i; j<n; j++) swap(a[i][j],a[p][j]); }
        for (int j=i+1; j<n; j++){
            data c=a[j][i]*Inv(a[i][i]);
            for (int k=i; k<n; k++) a[j][k]=a[j][k]-a[i][k]*c;
        }
    }
    for (int i=1; i<n; i++) cur=cur*a[i][i];
    if (rev) return (data){-cur.x,-cur.y};
    return cur;
}
inline void DFT(data* a){
    b[0]=a[0]*Uni+a[1]*w[0]+a[2]*w[0]*w[0];
    b[1]=a[0]*Uni+a[1]*w[1]+a[2]*w[1]*w[1];
    b[2]=a[0]*Uni+a[1]*w[2]+a[2]*w[2]*w[2];
    a[0]=b[0]; a[1]=b[1]; a[2]=b[2];
}
inline void IDFT(data* a){
    b[0]=a[0]*Inv(Uni)+a[1]*Inv(w[0])+a[2]*Inv(w[0]*w[0]);
    b[1]=a[0]*Inv(Uni)+a[1]*Inv(w[1])+a[2]*Inv(w[1]*w[1]);
    b[2]=a[0]*Inv(Uni)+a[1]*Inv(w[2])+a[2]*Inv(w[2]*w[2]);
    a[0]=b[0]*Inv3; a[1]=b[1]*Inv3; a[2]=b[2]*Inv3;
}
int main(){
    freopen("sum.in","r",stdin);
	freopen("sum.out","w",stdout);
	int Inv2=fastpow(2,mod-2); Inv3=(data){fastpow(3,mod-2),0};
    w[0]=(data){1,0}; w[1]=(data){mod-Inv2,Inv2}; w[2]=(data){mod-Inv2,mod-Inv2};
    for (int i=0; i<3; i++){ E[i][i]=(data){1,0}; DFT(E[i]); }
//    for (int j=0; j<3; j++) printf("%d : %d %d\n",j,w[j].x,w[j].y);
//    for (int i=0; i<3; i++)
//  		for (int j=0; j<3; j++) printf("%d %d : %d %d\n",i,j,E[i][j].x,E[i][j].y);
    scanf("%d%d",&n,&m); Pow[0]=1;
    for (int i=1; i<=10; i++) Pow[i]=Pow[i-1]*3;
    for (int i=1; i<=m; i++) scanf("%d%d%d",&U[i],&V[i],&W[i]);
    for (int i=0; i<=10; i++){
        for (int j=0; j<3; j++){
            memset(a,0,sizeof(a));
            for (int k=1; k<=m; k++){
                int u=U[k],v=V[k],w=(W[k]/Pow[i])%3;
                a[u][u]=a[u][u]+E[w][j]; a[v][v]=a[v][v]+E[w][j];
                a[u][v]=a[u][v]-E[w][j]; a[v][u]=a[v][u]-E[w][j];
            }
            res[j]=DET();
        }
        
        IDFT(res);
        ans=Plus(ans,1ll*Pow[i]*res[1].x%mod);
        ans=Plus(ans,2ll*Pow[i]*res[2].x%mod);
    }
    printf("%d\n",ans);
    return 0;
}