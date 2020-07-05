#include<iostream>
#include<cstdio>

using namespace std;

int a[11];

int m,n,k;
int main()
{
    scanf("%d%d",&m,&n);
    for(int i=m;i<=n;i++)
    {
        k=i;
        do
        {
            a[k%10]++;
            k=k/10;
        }while(k);
    }
    for(int j=0;j<=9;j++)
    printf("%d ",a[j]);
    return 0;
}