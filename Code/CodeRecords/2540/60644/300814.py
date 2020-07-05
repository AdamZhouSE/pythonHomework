#include<cstdio>
#include<cstring>
#include<algorithm>
struct act
{
    int s,t,num;
    friend bool operator <(act a,act b)
    {
        if(a.t!=b.t)
            return a.t<b.t;
        return a.s<b.s;
    }
}a[50010];
int End[111];
bool cmp(int x,int y)
{
    return x>y;
}
int main()
{
    int k,n,c;
    scanf("%d%d%d",&k,&n,&c);
    for(int i=1;i<=k;++i)
        scanf("%d%d%d",&a[i].s,&a[i].t,&a[i].num);
    std::sort(a+1,a+1+k);
    int sum=0;
    for(int i=1;i<=k;++i)
    {
        std::sort(End+1,End+1+c,cmp);
        for(int j=1;a[i].num&&j<=c;++j)
            if(End[j]<=a[i].s)
            {
                ++sum;
                End[j]=a[i].t;
                a[i].num--;
            }
    }
    printf("%d\n",sum);
    return 0;
}
