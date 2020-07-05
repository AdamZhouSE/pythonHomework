#include<bits/stdc++.h>
using  namespace std;
int main()
{
   int n,m,sum=0,r=0,col=0;
   char c;
   cin>>n>>m;
   for(int i=1;i<=n;i++)
    for(int j=1;j<=m;j++)
    {
        cin>>c;
        if (c=='B') r+=i,col+=j,sum++;
    }
        cout<<r/sum<<" "<<col/sum<<endl;
    return 0;
}