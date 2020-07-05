#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <cmath>
#define N 111
#define mod 1000000007
#define inv3 333333336
using namespace std;
int qp(int a,int b){
    int c=1;
    for(;b;b>>=1,a=1ll*a*a%mod)
        if(b&1)c=1ll*c*a%mod;
    return c;
}
struct num{
    int a,b;
    num(){}
    num(int x,int y){a=x;b=y;}
    num operator + (num x){return num((a+x.a)%mod,(b+x.b)%mod);}
    num operator - (num x){return num((a-x.a+mod)%mod,(b-x.b+mod)%mod);}
    num operator * (num x){
        return num(
            ((1ll*a*x.a-1ll*b*x.b)%mod+mod)%mod,
            ((1ll*a*x.b+1ll*b*x.a-1ll*b*x.b)%mod+mod)%mod);
        }
    num inv(){
        int val=qp(((1ll*a*b-1ll*a*a-1ll*b*b)%mod+mod)%mod,mod-2);
        return num(1ll*(b-a+mod)*val%mod,1ll*b*val%mod);
    }
    bool operator ! (){return !a&&!b;}
}A[N][N][3],w[3],det[3];
int n,m,ans,du[N*N],dv[N*N],dw[N*N];
int cnt;
void work(){
    num t;
    for(int d=0;d<=2;d++){
        det[d]=num(1,0);
        for(int k=1;k<n;k++){
            if(!A[k][k][d]){
                for(int i=k+1;i<=n;i++){
                    if(!(!A[i][k][d])){
                        det[d]=num(0,0)-det[d];
                        for(int j=k;j<=n;j++)swap(A[k][j][d],A[i][j][d]);
                        break;
                    }
                }
                if(!A[k][k][d]){det[d]=num(0,0);break;}
            }
            det[d]=det[d]*A[k][k][d];
            for(int i=k+1;i<n;i++){
                t=A[i][k][d]*A[k][k][d].inv();
                for(int j=k;j<=n;j++)
                    A[i][j][d]=A[i][j][d]-t*A[k][j][d];
            }
        }
    }
}
void dft(num *a){
    num b[3];
    b[0]=a[0]+a[1]+a[2];
    b[1]=a[0]+a[1]*w[1]+a[2]*w[2];
    b[2]=a[0]+a[1]*w[2]+a[2]*w[1];
    a[0]=b[0];a[1]=b[1];a[2]=b[2];
}
void add(int u,int v,int w){
    A[u][u][w]=A[u][u][w]+num(1,0);
    A[v][v][w]=A[v][v][w]+num(1,0);
    A[u][v][w]=A[u][v][w]-num(1,0);
    A[v][u][w]=A[v][u][w]-num(1,0);
}
void UPD(int &a,int b){
    a=(a+b>=mod)?(a+b-mod):(a+b);
}
int main(){
freopen("sum.in","r",stdin);
freopen("sum.out","w",stdout);
    w[0]=num(1,0);w[1]=num(0,1);
    w[2]=num(mod-1,mod-1);
    scanf("%d%d",&n,&m);
    for(int i=1;i<=m;i++)
        scanf("%d%d%d",&du[i],&dv[i],&dw[i]);
    for(int t=0,now=1;t<=8;t++,now=now*3){
        memset(A,0,sizeof A);
        for(int i=1;i<=m;i++){
            add(du[i],dv[i],dw[i]%3);
            dw[i]/=3;
        }
        for(int i=1;i<=n;i++)
            for(int j=1;j<=n;j++)
                dft(A[i][j]);
        cnt=t;
        work();            
        swap(w[1],w[2]);
        dft(det);
        swap(w[1],w[2]);
        UPD(ans,1ll*det[1].a*inv3%mod*now%mod);
        UPD(ans,1ll*det[2].a*inv3%mod*2*now%mod);
    }
    printf("%d\n",ans);
    return 0;
}