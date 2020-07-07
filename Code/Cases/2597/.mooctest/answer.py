#include <bits/stdc++.h>
#define maxn 1000001
using namespace std;
int v[maxn];//建立价格到美丽值的映射
long long tob,top;
priority_queue<int>qin;
priority_queue<int,vector<int>,greater<int> >qax;
void Add(){
    int x,y;
    cin>>x>>y;
    if (v[y]) return;//发现相同价格就返回
    qin.push(y);
    qax.push(y);
    v[y]=x;
    tob+=x,top+=y;
}
void Delin(){
    while(!qin.empty()&&!v[qin.top()]) qin.pop();
    if (!qin.empty()){
        int te=qin.top();
        tob-=v[te];
        top-=te;
        v[te]=0;
        qin.pop();
    }
}
void Delax(){
    while(!qax.empty()&&!v[qax.top()]) qax.pop();
    if (!qax.empty()){
        int te=qax.top();
        tob-=v[te];
        top-=te;
        v[te]=0;
        qax.pop();
    }
}
int main(){
    ios::sync_with_stdio(false);
    int q;
    cin>>q;
    while(q!=-1){
        if (q==1) Add();
        if (q==2) Delin();
        if (q==3) Delax();
        cin>>q;
    }
    cout<<tob<<" "<<top;
    return 0;
}