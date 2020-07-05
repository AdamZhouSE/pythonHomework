#include <cstdio>
int father[101];
int x[101],y[101];
int findfather(int x)
{
    if(father[x]==x)
        return x;
    else return father[x]=findfather(father[x]);
}
int main()
{
    int n,ans;
    scanf("%d",&n);
    for(int i=1;i<=n;i++)
        scanf("%d%d",&x[i],&y[i]);
    for(int i=1;i<=n;i++)
        father[i]=i;
    for(int i=1;i<=n;i++)
        for(int j=i+1;j<=n;j++)
            if(x[i]==x[j]||y[i]==y[j])
                father[findfather(i)]=findfather(j);
    ans=0;
    for(int i=1;i<=n;i++)
        if(father[i]==i)
            ans++;
    printf("%d\n",ans-1);
    return 0;
}