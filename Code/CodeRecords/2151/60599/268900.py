#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>

using namespace std;

const int N=110,P=1e9+7,inv2=P+1>>1;

struct E{
  int a,b;
  E(int _a=0,int _b=0):a(_a),b(_b){}
  friend E operator +(const E &a,const E &b){
    return E((a.a+b.a)%P,(a.b+b.b)%P);
  }
  friend E operator *(const E &a,const E &b){
    return E((1LL*a.a*b.a+P-3LL*a.b*b.b%P)%P,(1LL*a.a*b.b+1LL*a.b*b.a)%P);
  }
  friend E operator -(const E &a,const E &b){
    return E((a.a+P-b.a)%P,(a.b+P-b.b)%P);
  }
  bool empty(){
    return !a && !b;
  }
};

E w[3];

inline int Pow(int x,int y){
  int ret=1;
  for(;y;y>>=1,x=1LL*x*x%P) if(y&1) ret=1LL*ret*x%P;
  return ret;
}

inline E Inv(E a){
  E ret=E(a.a,P-a.b);
  int iv=Pow((1LL*a.a*a.a+3LL*a.b*a.b)%P,P-2);
  ret=E(1LL*ret.a*iv%P,1LL*ret.b*iv%P);
  return ret;
}

inline void DFT(E *a){
  static E tmp[3];
  for(int i=0;i<3;i++){
    E c=1; tmp[i]=0;
    for(int j=0;j<3;j++,c=c*w[i])
      tmp[i]=tmp[i]+c*a[j];
  }
  for(int i=0;i<3;i++) a[i]=tmp[i];
}

inline void IDFT(E *a){
  int iv=Pow(3,P-2);
  static E tmp[3];
  for(int i=0;i<3;i++){
    E c=1; tmp[i]=0;
    for(int j=0;j<3;j++,c=c*w[i])
      tmp[i]=tmp[i]+Inv(c)*a[j];
  }
  for(int i=0;i<3;i++) a[i]=1LL*tmp[i].a*iv%P;
}

int n,m,a[N*N],b[N*N],c[N*N];
int ans,pw[N];

E mat[3][N][N],unt[3][3];

inline E det(E a[N][N]){
  int f=0;
  for(int i=1;i<n;i++){
    int p=i; for(;a[p][i].empty() && p<n;p++);
    if(p>=n) return 0;
    if(p^i){ for(int j=i;j<n;j++) swap(a[p][j],a[i][j]); f^=1; }
    for(int j=i+1;j<n;j++){
      E g=Inv(a[i][i])*a[j][i];
      for(int k=i;k<n;k++)
    a[j][k]=a[j][k]-a[i][k]*g;
    }
  }
  E ret=1;
  for(int i=1;i<n;i++) ret=ret*a[i][i];
  if(f) ret=0-ret;
  return ret;
}

int main(){
  w[0]=E(1,0); E g=E(P-inv2,inv2);
  for(int i=1;i<3;i++) w[i]=w[i-1]*g;
  pw[0]=1;
  for(int i=1;i<=8;i++) pw[i]=pw[i-1]*3;
  for(int i=0;i<3;i++){
    unt[i][i]=1; DFT(unt[i]);
  }
  scanf("%d%d",&n,&m);
  for(int i=1;i<=m;i++)
    scanf("%d%d%d",&a[i],&b[i],&c[i]);
  for(int k=0;k<=8;k++){
    memset(mat,0,sizeof(mat));
    for(int i=1;i<=m;i++){
      int u=a[i],v=b[i],w=c[i]/pw[k]%3;
      for(int j=0;j<3;j++){
    mat[j][u][u]=mat[j][u][u]+unt[w][j];
    mat[j][v][v]=mat[j][v][v]+unt[w][j];
    mat[j][u][v]=mat[j][u][v]-unt[w][j];
    mat[j][v][u]=mat[j][v][u]-unt[w][j];
      }
    }
    E cur[3];
    for(int i=0;i<3;i++) cur[i]=det(mat[i]);
    IDFT(cur);
    for(int i=1;i<3;i++) ans=(ans+1LL*pw[k]*i*cur[i].a)%P;
  }
  printf("%d\n",ans);
  return 0;
}
