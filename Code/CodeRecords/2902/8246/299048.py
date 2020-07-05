#include<bits/stdc++.h>
using namespace std;
int n,d=1;  
int main()
{
    cin>>n;
    for(int i=1;i<=n;i++)
    {
        for(int j=1;j<=(n-d)/2;j++)
            cout<<'*';
        for(int j=1;j<=d;j++)
            cout<<'D';
        for(int j=1;j<=(n-d)/2;j++)
            cout<<'*';
        cout<<endl;
        if(i<=floor(n/2))d+=2;
        else d-=2;
    }
    return 0;
}