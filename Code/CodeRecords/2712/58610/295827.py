
#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
#include<vector>
#include<stdlib.h>
#include<queue>
#include<map>
#include<iomanip>
#include<math.h>
#include<sstream>
using namespace std;
typedef long long ll;
typedef double ld;
string mob[300010];
int num[300010];
int trip[300010][26];
int fail[300010];
int ans[300010];
int temp;
int n,siz;
void add(string s,int v)
{
    int now=0;
    for(int i=0; i<s.size(); i++)
    {
        int o=s[i]-'a';
        if(!trip[now][o])
            trip[now][o]=++siz;
        now=trip[now][o];
    }
    num[now]=v;
}
void getfail()
{
    int now=0;
    queue<int>que;
    for(int i=0; i<26; i++)
        if(trip[0][i])
            que.push(trip[0][i]),fail[trip[0][i]]=0;
    while(!que.empty())
    {
        int u=que.front();
        que.pop();
        for(int i=0; i<26; i++)
        {
            int v=trip[u][i];
            if(v)
            {
                fail[v]=trip[fail[u]][i];
                que.push(v);
            }
            else
                trip[u][i]=trip[fail[u]][i];
        }
    }
}
void query(string s)
{
    int now=0;
    for(int i=0; i<s.size(); i++)
    {
        now=trip[now][s[i]-'a'];
        for(int j=now; j; j=fail[j])
            ans[num[j]]++;
    }
}
int main()
{
    while(cin>>n&&n)
    {
        memset(num,0,sizeof(num));
        memset(ans,0,sizeof(ans));
        memset(trip,0,sizeof(trip));
        memset(fail,0,sizeof(fail));
        siz=0;
        for(int i=1; i<=n; i++)
        {
            cin>>mob[i];
            add(mob[i],i);
        }
        getfail();
        string k;
        cin>>k;
        query(k);
        temp=0;
        for(int i=1; i<=n; i++)
            if(ans[i]>temp)
                temp=ans[i];
        cout<<temp<<endl;
        for(int i=1; i<=n; i++)
            if(ans[i]==temp)
                cout<<mob[i]<<endl;
    }
    return 0;
}