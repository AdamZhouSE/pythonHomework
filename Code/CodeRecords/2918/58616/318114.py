#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <string>
#include <cstring>
using namespace std;
int a[200];
int main(){
    int n;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        int num;
        cin >> num;
        a[num]++;
    }
    int ans = 0,ret = 0,sum = 0;
    for (int i = 0; i < 101; i++)
    {
        sum += a[i];
        ret = (int)ceil(sum * 1.0 / (i + 1));
        ans = max(ans,ret);
    }  
    cout << ans << endl;
    return 0;
}