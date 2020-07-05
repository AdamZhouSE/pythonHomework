#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<queue>
const int Max=201;
char Map[Max][Max];
using namespace std;
int main()
{
    int i,j,n,m,num;
    while(cin>>n)
    {
        m=0;
        num=0;
        for(i=1;i<=n;i++)
        {
            for(j=1;j<=n;j++)
            {
                cin>>Map[i][j];
            }
        }
        for(i=1;i<=n;i++)
        {
            for(j=1;j<=n;j++)
            {
                num=0;
                if(i>1&&Map[i-1][j]=='o')
                    num++;
                if(i<n&&Map[i+1][j]=='o')
                    num++;
                if(j>1&&Map[i][j-1]=='o')
                    num++;
                if(j<n&&Map[i][j+1]=='o')
                    num++;
                if(num&1)
                {
                    m=1;
                    break;
                }
            }
            if(m==1)
                break;
        }
        if(!m)
            cout<<"YES"<<endl;
        else
            cout<<"NO"<<endl;
    }
    return 0;
}