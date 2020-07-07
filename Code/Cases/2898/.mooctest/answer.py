#include<bits/stdc++.h>
using namespace std;
int sum,l;
int main(){
    string s;
    cin>>l>>s;
    if(s=="0"){
        cout<<0;
        return 0;
    }
    cout<<1;
    for(int i=0;i<l;i++){
        if(s[i]=='0') sum++;
    }
    for(int i=1;i<=sum;i++){
        cout<<0;
    }
    return 0;
}