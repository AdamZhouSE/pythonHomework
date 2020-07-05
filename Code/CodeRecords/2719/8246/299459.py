#include<bits/stdc++.h>
using namespace std;
#define maxn 100000+10
int a[maxn],cnt,n,ans;
bool canc[maxn+maxn];
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin>>n;
    for(register int i=1;i<=n;i++){
        char c;
        cin>>c;
        if(c=='B'){
            cout<<ans<<endl;
        }
        if(c=='A'){
            int x,y,sum=0;
            cin>>x>>y;
            cnt++;
            ans++;
            for(register int i=x;i<=y;i++){
                if(a[i]){
                    if(canc[a[i]]==0){
                        ans--;
                        canc[a[i]]=1;
                        sum++;
                    }
                }
                a[i]=cnt;
            }
            cout<<sum<<endl;
        }
    }
    return 0;
}