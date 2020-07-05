#include "iostream"
using namespace std;
const int Max=1e3+10;
int a[Max],ans[Max],flag[Max];
int main()
{
    int n,tot=0;
    cin>>n;
    for(int i=1;i<=n;i++)
        cin>>a[i];
    for(int i=n;i>=1;i--){
        if(!flag[a[i]]){
            flag[a[i]]=1;
            ans[tot++]=a[i];
        }
    }
    cout<<tot<<endl;
    for(int i=tot-1;i>=0;i--){
        cout<<ans[i];
        if(i!=0)
            cout<<" ";
    }
    cout<<endl;
    return  0;
}