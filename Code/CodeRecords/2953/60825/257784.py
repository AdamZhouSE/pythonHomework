#include<iostream>
using namespace std;
int gcd(int x,int y)
{
    if(y==1) return x-1;
    if(x==0) return 1000;
    if(y==0) return 1000;
    if(x==y) return 1000;
    return gcd(y,x%y)+x/y;
}
int main()
{
    int n,ans;
    cin>>n;
    ans=n-1;
    for(int i=2;i<n;i++) 
        ans=min(gcd(n,i),ans);
    cout<<ans;
}