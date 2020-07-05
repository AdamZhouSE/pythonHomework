#include<iostream>
#include<cstdio>
#include<cstring>
#define maxn 105
using namespace std;
int a[maxn];
int main()
{
    int i,n;
    while(scanf("%d",&n)==1)
    {
        memset(a,0,sizeof(a));//因为1=<a[i]<=1000，所以初始化可以直接用0
        for(i=0;i<n;i++)
            cin>>a[i];
        int p=1;
        while(a[p]>a[p-1])//顺序要对
            p++;
        while(a[p]==a[p-1])
            p++;
        while(a[p]<a[p-1])
            p++;
        if(p>n)//这里p只可能大于n或小于n
            cout<<"YES"<<endl;
        else cout<<"NO"<<endl;
    }
    return 0;
}