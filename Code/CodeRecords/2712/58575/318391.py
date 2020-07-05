#include <iostream>
#include <cstdio>
#include <cstring>
#include <queue>
#include <algorithm>
#define maxn 1000000
using namespace std;
struct tree
{
    int fail;
    int vis[26];
    int end;
} ac[maxn];
int cnt=0;
struct node
{
    int num;
    int pos;
} ans[maxn];
string s[maxn];
bool cmp(node a,node b)
{
    if(a.num==b.num)
        return a.pos<b.pos;
    return a.num>b.num;
}
void clean(int x)
{
    memset(ac[x].vis,0,sizeof(ac[x].vis));
    ac[x].fail=0;
    ac[x].end=0;
}
void build(string s,int no)
{
    int l=s.length();
    int now=0;
    for(int i=0; i<l; i++)
    {
        if(!ac[now].vis[s[i]-'a'])
    {
        ac[now].vis[s[i]-'a']=++cnt;
            clean(cnt);
        }
        now=ac[now].vis[s[i]-'a'];
    }
    ac[now].end=no;
}
void getfail()
{
    queue<int > q;
    for(int i=0; i<26; i++)
    {
        if(ac[0].vis[i])
        {
            ac[ac[0].vis[i]].fail=0;
            q.push(ac[0].vis[i]);
        }
    }
    while(!q.empty())
    {
        int u=q.front();
        q.pop();
        for(int i=0; i<26; i++)
        {
            if(ac[u].vis[i])
            {
                ac[ac[u].vis[i]].fail=ac[ac[u].fail].vis[i];
                q.push(ac[u].vis[i]);
            }
            else
                ac[u].vis[i]=ac[ac[u].fail].vis[i];
        }
    }
}
int acquery(string s)
{
    int l=s.length();
    int now=0;
    int answer=0;
    for(int i=0; i<l; i++)
    {
        now=ac[now].vis[s[i]-'a'];
        for(int t=now; t; t=ac[t].fail)
            ans[ac[t].end].num++;
    }
    return answer;
}
int main()
{
    int n;
    while(1)
    {
        cin>>n;
        if(!n)break;
        cnt=0;
        clean(0);
        for(int i=1; i<=n; i++)
        {
            cin>>s[i];
            ans[i].num=0;
            ans[i].pos=i;
            build(s[i],i);
        }
        ac[0].fail=0;
        getfail();
        cin>>s[0];
        acquery(s[0]);
        sort(ans+1,ans+1+n,cmp);
        cout<<ans[1].num<<endl;
        cout<<s[ans[1].pos]<<endl;
        for(int i=2; i<=n; i++)
        {
            if(ans[i].num==ans[i-1].num)
                cout<<s[ans[i].pos]<<endl;
            else
                break;
        }
    }
    return 0;
}