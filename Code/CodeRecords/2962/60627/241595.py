#include <iostream>
#include <queue>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <map>
#define INF 0x3f3f3f3f
#define FRE() freopen("in.txt","r",stdin)
 
using namespace std;
typedef long long ll;
typedef pair<int,int> P;
const int maxn = 50010;
map<string,int> mp;
string str;
int vis[maxn];
 
int Judge(int sum, int p){
    sum %= p;
    if(mp.count(str)){//重复出现
        return sum;
    }
    if(vis[sum] && mp[str] == 0){//发生冲突
        int k = 1,tmp = sum;
        while(vis[sum]){
            sum = (tmp+k*k)%p;
            if(!vis[sum])break;
            sum = (tmp-k*k+p)%p;
            k++;
        }
        vis[sum] = 1;
        mp[str] = sum;
        return sum;
    }
    else if(!vis[sum] && mp[str] == 0){
        vis[sum] = 1;
        mp[str] = sum;
        return sum;
    }
}
 
 
 
int main() {
    //FRE();
    int n,p;
    cin>>n>>p;
    memset(vis,0,sizeof(vis));
    for(int i = 0; i<n; i++) {
        cin>>str;
        int len = str.size(),sum = 0;
        if(len>3) {
            for(int j = len-3; str[j]; j++) {
                int temp = str[j]-'A';
                sum = sum*32 + temp;
            }
        } else {
            for(int j = 0; str[j]; j++) {
                int temp = str[j] - 'A';
                sum = sum*32 + temp;
            }
        }
        int tt = Judge(sum, p);
        if(i == 0)
            cout<<tt;
        else
            cout<<" "<<tt;
    }
    cout<<endl;
    return 0;
}