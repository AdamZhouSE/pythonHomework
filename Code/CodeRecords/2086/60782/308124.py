#include <iostream>
#include <stdio.h>
#include <stack>
#include <queue>
#include <string.h>
#include <math.h>
#include <algorithm>
using namespace std;
int f[200005];
int R,P;
struct out
{
    int a,b;
    long long c;
};
out e[500004];
bool cmp(out x,out y)
{
    return x.c<y.c;
}
void tinin()
{
    for(int j=0; j<=P; j++)
    {
        f[j]=j;
    }
}
int Find(int x)
{
    if(f[x]==x)
    {
        return x;
    }
    return f[f[x]]=Find(f[x]);
}
int combin(int x,int y)
{
    x=Find(x);
    y=Find(y);
    if(x!=y)
    {
        f[x]=y;
        return 1;
    }
    return 0;
}
int main()
{
    int k,i;
    long long sum=0;
    scanf("%d%d",&P,&R);
        for(i=0; i<R; i++)
        {
            scanf("%d%d%lld",&e[i].a,&e[i].b,&e[i].c);
        }
        sort(e,e+R,cmp);
        tinin();
        k=0;
        sum=0;
        for(i=0; i<R; i++)
        {
            if(combin(e[i].a,e[i].b))
            {
                sum=sum+e[i].c;
                k++;
            }
            if(k==P-1)
                break;
        }
        printf("%lld",sum);
    return 0;
}