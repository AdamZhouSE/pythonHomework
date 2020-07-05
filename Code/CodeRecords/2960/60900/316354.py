#include<map>
#include<cmath>
#include<stack>
#include<queue>
#include<cstdio>
#include<cctype>
#include<vector>
#include<cstdlib>
#include<cstring>
#include<iostream>
#include<algorithm>
using namespace std;
typedef double dl;
const dl pi=acos(-1.0);
const dl eps=0.5;
const int N=2e6+5;
struct complex{
    dl x,y;
    complex(dl xx=0.0,dl yy=0.0){
    x=xx;y=yy;
    }
    complex operator +(const complex &b)const{
    return complex(x+b.x,y+b.y);
    }
    complex operator -(const complex &b)const{
    return complex(x-b.x,y-b.y);
    }
    complex operator *(const complex &b)const{
    return complex(x*b.x-y*b.y,x*b.y+y*b.x);
    }
};
void FFT(complex a[],int n,int on){
    for(int i=1,j=n>>1;i<n-1;i++){
    if(i<j)swap(a[i],a[j]);
    int k=n>>1;
    while(j>=k){j-=k;k>>=1;}
    if(j<k)j+=k;
    }
    for(int i=2;i<=n;i<<=1){
    complex res(cos(-on*2*pi/i),sin(-on*2*pi/i));
    for(int j=0;j<n;j+=i){
        complex w(1,0);
        for(int k=j;k<j+i/2;k++){
        complex u=a[k],t=w*a[k+i/2];
        a[k]=u+t;a[k+i/2]=u-t;
        w=w*res;
        }
    }
    }
    if(on==-1)
    for(int i=0;i<n;i++)a[i].x/=n;
}
int n,m,a[N],b[N];
complex f[N],A[N],B[N];
char s1[N],s2[N];
int main(){
    scanf("%d%d%s%s",&n,&m,s1,s2);
    for(int i=0,j=n-1;i<j;i++,j--)swap(s1[i],s1[j]);
    for(int i=0;i<n;i++){
    if(s1[i]!='*')a[i]=s1[i]-'a'+1;
    else a[i]=0;
    }
    for(int i=0;i<m;i++){
    if(s2[i]!='*')b[i]=s2[i]-'a'+1;
    else b[i]=0;
    }
    int len=1;
    while(len<m)len<<=1;

    for(int i=0;i<len;i++)
    A[i]=complex(a[i]*a[i]*a[i],0),B[i]=complex(b[i],0);
    FFT(A,len,1);FFT(B,len,1);
    for(int i=0;i<len;i++)f[i]=f[i]+A[i]*B[i];
    
    for(int i=0;i<len;i++)
    A[i]=complex(a[i]*a[i],0),B[i]=complex(b[i]*b[i],0);
    FFT(A,len,1);FFT(B,len,1);
    for(int i=0;i<len;i++)f[i]=f[i]-A[i]*B[i]*complex(2,0);

    for(int i=0;i<len;i++)
    A[i]=complex(a[i],0),B[i]=complex(b[i]*b[i]*b[i],0);
    FFT(A,len,1);FFT(B,len,1);
    for(int i=0;i<len;i++)f[i]=f[i]+A[i]*B[i];

    FFT(f,len,-1);
    int ans=0;
    for(int i=n-1;i<m;i++)if(f[i].x<eps)ans++;
    printf("%d\n",ans);
    if(ans){
    for(int i=n-1;i<m;i++)if(f[i].x<eps)printf("%d ",i-n+2);
    puts("");
    }
    return 0;
}