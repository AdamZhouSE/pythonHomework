#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<map>
#include<set>
#include<vector>
#include<queue>
#include<list>
//#include<unordered_map>
#include<stack>
using namespace std;
#define ll long long 
const int mod=1e9+7;
const int inf=1e9+7;
 
const int maxn=1e3+10;
 
string str[maxn];
 
int point[maxn];
 
int main()
{
    ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);
    
    int n,m;
    
    cin>>n>>m;
    
    for(int i=0;i<n;i++)
        cin>>str[i];
    
    for(int i=0;i<m;i++)
        cin>>point[i];
    
    map<char,int>book;
    
    ll int sum=0;
    for(int i=0;i<m;i++)
    {
        book.clear();
        ll int maxx=-1;
        for(int j=0;j<n;j++)
        {
            book[str[j][i]]++;
            
            if(book[str[j][i]]>maxx)
            {
                maxx=book[str[j][i]];
            }
        }
        sum+=point[i]*maxx;
    
    }
    
    cout<<sum<<endl;
    
    return 0;
}