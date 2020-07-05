#include <iostream>
#include <algorithm>
#include <cstring>
#include <vector>
using namespace std; 
int n, arr[1005];
int res;
int main() {
    cin >> n;
    for(int i = 1; i<=n; i++){
        cin >> arr[i];
    }
    for(int i = 2; i<n; i++){
        if(arr[i+1] == 1 && arr[i-1] == 1 && arr[i] == 0){
            arr[i+1] = 0;
            res ++;
        }
    }
    cout << res << endl;
    return 0;
}