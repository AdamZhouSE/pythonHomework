//简单的贪心。显然能够写的数字位数越多就越大，其次是数字的字面值尽量大。
//最多能写多少位数字，找到最小的那个，求出剩余油漆，然后从大到小枚举数字，
//看看能否换上这个数字，能换几个，换了之后更新剩余油漆。
#include<bits/stdc++.h>
using namespace std;
const int inf=0x7fffffff;
int n,v,a[1000006],ans[1000006];
int main()
{
    cin>>v;
    int mini,minn=inf;
    for(int i=1;i<=9;i++){
        cin>>a[i];
        if(a[i]<minn){
            minn=a[i];
            mini=i;
        }
    }
    int maxn=v/a[mini];
    int vv=v%a[mini];
    queue<int>q;
    for(int i=1;i<=maxn;i++) q.push(mini);
    if(maxn>0){
        for(int i=9;i>=1;i--){
            int sum=vv,tmp=0;
            for(int j=1;j<=maxn;j++){
                if(q.front()>i) break;
                sum+=a[q.front()];
                if(sum<j*a[i]){
                    sum-=a[q.front()];
                    break;
                }
                q.pop();tmp=j;
            }
            if(tmp) vv=sum%a[i];
            while(tmp--) q.push(i);
        }
    }
    if(maxn==0) cout<<"-1\n";
    else{
        int cnt=0;
        while(!q.empty()){
            ans[cnt++]=q.front();q.pop();
        }
        sort(ans,ans+cnt);
        for(int i=cnt-1;i>=0;i--) cout<<ans[i];
        cout<<endl;
    }
    return 0;
}