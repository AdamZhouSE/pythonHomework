#include <iostream>
using namespace std;
int main(){
    int T = 0;
    cin >> T;
    for (int i = 0; i < T; ++i){
        unsigned int n = 0;
        cin >> n;
        cout << ~n << endl;
    }
}