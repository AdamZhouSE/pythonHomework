#include<iostream>
#include<algorithm>
using namespace std;
int n,m,ans;
int a[10005],t[10005];
int main(){
    cin>>n>>m;
    for(int i=1;i<=n;i++)
        cin>>a[i];
    for(int i=1;i<=n;i++)
        t[i]=a[i];
    char opt;
    int x,y,z;
    for(int i=1;i<=m;i++){
        cin>>opt;
        if(opt=='Q'){
            cin>>x>>y>>z;
            nth_element(a+x,a+z+x-1,a+y+1);
            cout<<a[z+x-1]<<endl;
            for(int i=1;i<=n;i++)
                a[i]=t[i];
        }
        else if(opt=='C'){
            cin>>x>>y;
            t[x]=a[x]=y;
        }
    }
    return 0;
}