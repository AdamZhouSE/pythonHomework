#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <algorithm>
#define INF 2147483647
using namespace std;

int ans=INF,n;

void check(int a,int b,int step){
    if(b==0){
        if(a==1)ans=min(ans,step);
        return;
    }
    if(a<b)swap(a,b);
    check(b,a%b,step+a/b);
}

int main()
{
    scanf("%d",&n);
    if(n==1){
        printf("%d",0);
        return 0;
    }
        
    for(int i=1;i<n;i++)
        check(n,i,0);
    printf("%d",ans-1);
    return 0;
}