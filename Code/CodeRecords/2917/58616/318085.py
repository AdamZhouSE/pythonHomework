#include <iostream>
#include <cstdio>
#include <cstring>
#include <queue>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
using namespace std;
typedef long long ll;
int main()
{
map<ll,ll>ans,pos;
map<pair<ll,ll>,ll>inf;
ll x,y,n,cnt=0;
cin>>n;
while(n--)
{
cin>>x>>y;
cnt+=ans[x]++;
cnt+=pos[y]++;
cnt-=inf[make_pair(x,y)]++;//减去重复的
}
cout<<cnt<<endl;
}