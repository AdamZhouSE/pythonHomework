#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
 
#define mod 1000000007
int n,m;
char s[1005][1005],tmp[1005][1005];
long long k;
struct Matrix{
    long long mat[5][5];
    Matrix(){memset(mat,0,sizeof(mat));}
    Matrix operator*(const Matrix &b)const{
        Matrix c;
        for(int i=1;i<=2;i++)
        for(int j=1;j<=2;j++){
            for(int k=1;k<=2;k++)
                c.mat[i][j]+=mat[i][k]*b.mat[k][j];
            c.mat[i][j]%=mod;
        }
        return c;
    }
    Matrix operator^(long long x)const{
        Matrix a(*this),ans;
        for(int i=1;i<=2;i++)ans.mat[i][i]=1;
        while(x){
            if(x&1)ans=ans*a;
            x>>=1,a=a*a;
        }
        return ans;
    }
}mat;
 
int qpow(int x,long long y){
    int ans=1;
    while(y){
        if(y&1)ans=1LL*ans*x%mod;
        y>>=1,x=1LL*x*x%mod;
    }
    return ans;
}
 
bool check(){
    for(int i=1;i<=n;i++)
        if(s[i][1]=='#'&&s[i][m]=='#')return true;
    return false;
}
 
void turn(){
    for(int i=1;i<=n;i++)
    for(int j=1;j<=m;j++)
        tmp[m-j+1][i]=s[i][j];
    swap(n,m);
    memcpy(s,tmp,sizeof(s));
}
 
int main(){
    scanf("%d%d%lld",&n,&m,&k);
    int x=0,y=0,z=0;
    for(int i=1;i<=n;i++){
        scanf("%s",s[i]+1);
        for(int j=1;j<=m;j++)x+=s[i][j]=='#';
    }   
    bool a=check(),b=(turn(),check());turn();
    if(a&&b)return printf("1"),0;
    else if(!a&&!b)return printf("%d",qpow(x,k-1)),0;
    else if(b)turn();
    for(int i=1;i<=n;i++)
        z+=s[i][1]=='#'&&s[i][m]=='#';
    for(int i=1;i<=n;i++)
    for(int j=1;j<m;j++)y+=s[i][j]=='#'&&s[i][j+1]=='#';
    mat.mat[1][1]=x,mat.mat[1][2]=y,mat.mat[2][2]=z;
    mat=mat^(k-1);
    printf("%lld\n",(mat.mat[1][1]-mat.mat[1][2]+mod)%mod);
}