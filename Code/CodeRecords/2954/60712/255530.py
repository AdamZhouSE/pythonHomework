#include <bits/stdc++.h>#define setIO(s) freopen(s".in","r",stdin) #define maxn 30 #define mod 1000000007 #define ll long long using namespace std;char str[100003]; struct matrix{    ll mat[30][30];      int n,m; }; void init(matrix &a){    for(int i=0;i<a.n;++i)         for(int j=0;j<a.m;++j) a.mat[i][j]=0; }void get(matrix &a){    init(a);    for(int i=0;i<a.n;++i) a.mat[i][i]=1; }matrix operator*(matrix a,matrix b){    matrix c;     c.n=a.n,c.m=b.m;     init(c);     for(int i=0;i<a.n;++i)         for(int j=0;j<b.m;++j)             for(int k=0;k<a.m;++k)                c.mat[i][j]=((a.mat[i][k]*b.mat[k][j])%mod+c.mat[i][j])%mod;     return c; }matrix operator^(matrix a,ll y){    matrix c;     c.n=a.n,c.m=a.m;     get(c);     while(y){        if(y&1) c=c*a;                a=a*a;         y>>=1;     }    return c; }int main(){     int k;      ll n;     scanf("%lld%s",&n,str),k=strlen(str);      matrix a,b;     b.n=26,b.m=26;    a.n=1,a.m=26;       for(int i=0;i<26;++i) a.mat[0][i]=1;     for(int i=0;i<26;++i)         for(int j=0;j<26;++j) b.mat[i][j]=1;                  for(int i=1;i<k;++i) {                int d=str[i]-'a',c = str[i-1]-'a';        b.mat[c][d]=0;     }    b=b^(n-1);              a=a*b;     ll ans=0;     for(int i=0;i<26;++i) ans+=a.mat[0][i],ans%=mod;     printf("%lld",ans);     return 0; }
