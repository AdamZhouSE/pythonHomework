#include<cstdio>
using namespace std;
int a[6000],b[10000],k,t;
bool g;
int ss(int p,int x)
{
    if (p>t)
    {
        int m=x;
        for (int i=1;i<k;i++)
        {
            m=(m&(t/2-1))*2+b[i];
            if (a[m]!=0)
                return 0;
        }
        for (int i=1;i<=t-1;i++)
            printf("%d",b[i]);
        printf("%d\n",b[t]);
        g=true;
    }
    if (a[(x&(t/2-1))*2]==0)
    {
        a[(x&(t/2-1))*2]=1;
        ss(p+1,(x&(t/2-1))*2);
        if (g) return 0;
        a[(x&(t/2-1))*2]=0;
    }
    if (a[(x&(t/2-1))*2+1]==0)
    {
        a[(x&(t/2-1))*2+1]=1;
        b[p]=1;
        ss(p+1,(x&(t/2-1))*2+1);
        if (g) return 0;
        b[p]=0;
        a[(x&(t/2-1))*2+1]=0;
    }
}
int main()
{
    scanf("%d",&k);
    t=1;
    for (int i=1;i<=k;i++)
        t=t*2;
    printf("%d ",t);
    a[0]=1;
    g=false;
    ss(k+1,0);
}