// 别人的cpp代码
#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<cstring>
#include<map>
#define Ll long long
using namespace std;
map<int,int>F;
int q[300000],top;
int n,m,now,x,ans;
char c;
int main()
{
    scanf("%d%d",&n,&m);
    for(int i=1;i<=n;i++){
        scanf("%d",&x);
        cin>>c;
        if(c=='R'){
            q[++top]=now;
            F[q[top]]++;
            q[++top]=now+x;
            F[q[top]]--;
            now+=x;
        }else{
            q[++top]=now-x;
            F[q[top]]++;
            q[++top]=now;
            F[q[top]]--;
            now-=x;
        }
    }
    sort(q+1,q+top+1);
    now=F[q[1]];
    for(int i=2;i<=top;i++)
        if(q[i]!=q[i-1]){
            if(now>=m)ans+=q[i]-q[i-1];
            now+=F[q[i]];
        }
    printf("%d",ans);
}