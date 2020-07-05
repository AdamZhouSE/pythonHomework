//Too Difficult
#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

bool Finish_read;

template<class T>inline void read(T &x){Finish_read=0;x=0;int f=1;char ch=getchar();while(!isdigit(ch)){if(ch=='-')f=-1;if(ch==EOF)return;ch=getchar();}while(isdigit(ch))x=x*10+ch-'0',ch=getchar();x*=f;Finish_read=1;}

template<class T>inline void print(T x){if(x/10!=0)print(x/10);putchar(x%10+'0');}

template<class T>inline void writeln(T x){if(x<0)putchar('-');x=abs(x);print(x);putchar('\n');}

template<class T>inline void write(T x){if(x<0)putchar('-');x=abs(x);print(x);}

/*================Header Template==============*/

const int N=1e4+50;

int n,len;

ll ans;

int a[N],block[N];

ll fac[N];

/*==================Define Area================*/

int Judge(int l,int k) {

    for(int i=1;i<block[k];i++) {

        if(a[l+i-1]+1!=a[l+i]) return 0;

    }

    return 1;

} 

 

void Swap(int l,int r,int k) {

    for(int i=0;i<block[k];i++) 

        swap(a[l+i],a[r+i]);

} 

 

void Dfs(int k,int nw) {

    if(k==n+1) {

        ans+=fac[nw];

        return ;

    }

    int pos1=0,pos2=0;

    for(int i=1;i<=len;i+=block[k]) {

        if(!Judge(i,k)) {

            if(!pos1) pos1=i;

            else if(!pos2) pos2=i;

            else return ;

        }

    }

    if(!pos1&&!pos2) Dfs(k+1,nw);

    else if(pos1&&!pos2) {

        Swap(pos1,pos1+block[k-1],k-1);

        Dfs(k+1,nw+1);

        Swap(pos1,pos1+block[k-1],k-1);

    }

    else {

        for(int i=0;i<2;i++) {

            for(int j=0;j<2;j++) {

                Swap(pos1+i*block[k-1],pos2+j*block[k-1],k-1);

                if(Judge(pos1,k)&&Judge(pos2,k)) {

                    Dfs(k+1,nw+1);

                    Swap(pos1+i*block[k-1],pos2+j*block[k-1],k-1);

                    break;

                }

                Swap(pos1+i*block[k-1],pos2+j*block[k-1],k-1);

            }

        }

    }

    return ;

}

 

int main() {

    read(n);

    block[0]=1,fac[0]=1;

    for(int i=1;i<=n;i++) block[i]=block[i-1]<<1,fac[i]=fac[i-1]*i;

    len=1<<n;

    for(int i=1;i<=len;i++) read(a[i]);

    Dfs(1,0);

    printf("%lld\n",ans);

    return 0;

}