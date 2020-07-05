#include <bits/stdc++.h>
using namespace std;
typedef long long LL;

const int N=1e3+50,mod=1e9+7;
inline int add(int x,int y) {return (x+y>=mod) ? (x+y-mod) : (x+y);}
inline int dec(int x,int y) {return (x-y<0) ? (x-y+mod) : (x-y);}
inline int mul(int x,int y) {return (LL)x*y%mod;}
inline int power(int a,int b,int rs=1) {for(;b;b>>=1,a=mul(a,a)) if(b&1) rs=mul(rs,a); return rs;}
struct matrix {
    int a[2][2];
    matrix(int t=0) {memset(a,0,sizeof(a)); a[0][0]=a[1][1]=t;}
    friend inline matrix operator *(const matrix &a,const matrix &b) {
        matrix c;
        for(int i=0;i<2;i++) for(int k=0;k<2;k++) for(int j=0;j<2;j++) c.a[i][j]=add(c.a[i][j],mul(a.a[i][k],b.a[k][j]));
        return c;
    }
    friend inline matrix power(matrix a,LL b) {
        matrix rs(1);
        for(;b;b>>=1,a=a*a) if(b&1) rs=rs*a;
        return rs;
    }
};

int h,w,b1,b2,c1,c2,cnt,t;
char s[N][N]; LL k;
int main() {
    cin>>h>>w>>k; if(k<=1) {return puts("1"),0;}
    for(int i=1;i<=h;i++) cin>>(s[i]+1);
    for(int i=1;i<=h;i++) if(s[i][1]=='#' && s[i][w]=='#') ++c1;
    for(int i=1;i<=w;i++) if(s[1][i]=='#' && s[h][i]=='#') ++c2;
    for(int i=1;i<=h;i++) for(int j=1;j<=w;j++) if(s[i][j]=='#') ++cnt;
    for(int i=1;i<=h;i++) for(int j=1;j<=w;j++) if(s[i][j]=='#') b1+=(s[i][j]==s[i][j+1]), b2+=(s[i][j]==s[i+1][j]);
    if(c1&&c2) return puts("1"),0;
    else if(!c1 && !c2) return cout<<power(cnt,k-1),0;
    else {
        if(!c1) swap(c1,c2), swap(b1,b2);
        matrix A; A.a[0][0]=cnt; A.a[0][1]=0; A.a[1][0]=b1; A.a[1][1]=c1;
        A=power(A,k-1); cout<<dec(A.a[0][0],A.a[1][0])<<endl;
    }
}
