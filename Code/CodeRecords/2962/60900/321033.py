#include<bits/stdc++.h>
using namespace std;
typedef long long LL;
int n,cap;
const int maxn = 50100;
int Hashvis[maxn];
int ans[maxn];
set<string> same;
map<string,int> maps;
int GetHash(string t)
{
    int ans = 0;
    for(int i=0;i<min((int)t.length(),3);i++)
    {
        ans+=((int)pow(32,i)*((int)(t[i]-‘A‘)));
    }
    int tans = ans;
    ans%=cap;
    int k = 1;
    while(Hashvis[ans]) //平方探测法
    {
        ans = (tans + k*k)%cap;
        if(!Hashvis[ans]) break;
        ans = (tans - k*k + cap)%cap;
        k++;
    }
    Hashvis[ans] = 1;
    return ans;
}
int main()
{
    memset(ans,0,sizeof(ans));
    memset(Hashvis,0,sizeof(Hashvis));
    scanf("%d%d",&n,&cap);
    string s;
    for(int i=0;i<n;i++)
    {
        cin>>s;
        reverse(s.begin(),s.end());
        if(same.count(s)) ans[i] = maps[s]; //相同判断
        else{
        same.insert(s);
        ans[i] = GetHash(s);
        maps[s] = ans[i];
        }
    }
    for(int i=0;i<n;i++)
        printf("%d%c",ans[i],i==n-1?‘\n‘:‘ ‘);
}