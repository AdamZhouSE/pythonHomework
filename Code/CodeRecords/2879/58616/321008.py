#include<stdio.h>
#include<string.h>
int main()
{
    int n,a,b,x[100000],y[100000];
    memset(x,0,sizeof(x));
    memset(y,0,sizeof(y));
    scanf("%d",&n);
    int f[100000],k=0;
    memset(f,0,sizeof(f));
    for(int i=0; i<n*n; i++)
    {
        scanf("%d%d",&a,&b);
        if(x[a]==0&&y[b]==0)
        {
            x[a]=1;
            y[b]=1;
            f[k++]=i;
        }
    }
    for(int i=0;i<k;i++)
    {
        if(i==0)
            printf("%d",f[i]+1);
        else
            printf(" %d",f[i]+1);
    }
    printf("\n");
    return 0;
}