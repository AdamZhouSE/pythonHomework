#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <string>
#include <vector>
#include <bitset>
#include <stack>
#include <cmath>
#include <deque>
#include <queue>
#include <list>
#include <set>
#include <map>
#define mem(a, b) memset(a, b, sizeof(a))
typedef long long ll;
const double PI = acos(-1);
const int INF = 0x3f3f3f3f;
const int MAXN = 105;
using namespace std;
ll sum;

int main(){
    int n, m;
    while(cin >> n >> m){
        priority_queue<int, vector<int>, greater<int> > que;
        sum = 0;
        while(n--){
            int a, b;
            cin >> a >> b;
            sum += a;
            que.push(b-a);
        }
        int ans = 0;
        while(!que.empty()){
            if(sum <= m){
                break;
            }
            else{
                ans++;
                sum += que.top();
                que.pop();
            }
        }
        if(sum <= m){
            cout << ans << endl;
        }
        else{
            cout << "-1" << endl;
        }
    }
}