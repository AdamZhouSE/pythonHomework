#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>
#include <cctype>

using namespace std;

int read()
{
    int x=0,f=1;
    char ch=getchar();
    while (!isdigit(ch)) f=ch=='-'?-1:f,ch=getchar();
    while (isdigit(ch)) x=x*10+ch-'0',ch=getchar();
    return x*f;
}

const int P=1000000007;
const int N=305;

typedef pair<int,int> PI;

#define mkp(a,b) make_pair(a,b)
#define ft first
#define sd second

int sqr(int x){return 1ll*x*x%P;}

int quick_power(int x,int y)
{
    int ret=1;
    for (;y;y>>=1,x=1ll*x*x%P) if (y&1) ret=1ll*ret*x%P;
    return ret;
}

PI operator+(PI x,PI y){return mkp((x.ft+y.ft)%P,(x.sd+y.sd)%P);}
PI operator+=(PI &x,PI y){return x=x+y;}
PI operator-(PI x){return mkp(P-x.ft,P-x.sd);}
PI operator-(PI x,PI y){return x+(-y);}
PI operator-=(PI &x,PI y){return x=x-y;}
PI operator*(PI x,PI y){return mkp(1ll*x.ft*y.ft%P,(1ll*x.ft*y.sd%P+1ll*x.sd*y.ft%P)%P);}
PI operator*=(PI &x,PI y){return x=x*y;}
PI operator/(PI x,PI y)
{
    int inv=quick_power(y.ft,P-2);
    return mkp(1ll*x.ft*inv%P,1ll*(1ll*x.sd*y.ft%P-1ll*x.ft*y.sd%P+P)%P*sqr(inv)%P);
}

PI tmp[N][N];

struct matrix
{
    PI num[N][N];
    int s;

    PI det()
    {
        memcpy(tmp,num,sizeof num);bool sig=1;
        for (int i=0;i<s;++i)
        {
            if (!tmp[i][i].ft)
                for (int j=i+1;j<s;++j)
                    if (tmp[j][i].ft)
                    {
                        sig^=1;
                        for (int k=i;k<s;++k) swap(tmp[i][k],tmp[j][k]);
                        break;
                    }
            if (!tmp[i][i].ft) continue;
            PI inv=mkp(1,0)/tmp[i][i],mul;
            for (int j=i+1;j<s;++j)
                if (tmp[j][i].ft)
                {
                    mul=tmp[j][i]*inv;
                    for (int k=i;k<s;++k) tmp[j][k]-=tmp[i][k]*mul;
                }
        }
        PI ret=mkp(1,0);
        for (int i=0;i<s;++i) ret*=tmp[i][i];
        return sig?ret:-ret;
    }
}Kir;

int n,m;

int main()
{
    freopen("calc.in","r",stdin),freopen("calc.out","w",stdout);
    n=read(),m=read(),Kir.s=n;
    for (int i=1,x,y,z;i<=m;++i)
    {
        x=read()-1,y=read()-1,z=read(),swap(x,y);
        Kir.num[y][y]+=mkp(1,z),Kir.num[x][y]-=mkp(1,z);
    }
    --Kir.s,printf("%d\n",Kir.det().sd);
    fclose(stdin),fclose(stdout);
    return 0;
}
