#include<bits/stdc++.h>
using namespace std;
const int N=100009;
const int M=20000009;
const int F=1000009;
const double eps=1e-9;
struct qaq{
    int a[M],n;
    qaq(){
        memset(a,0,sizeof a);
        n=2*F;
    }
    void add(int x,int v){
        for(;x<=n;x+=x&-x) a[x]+=v;
    }
    int query(int x){
        int ans=0;
        for(;x;x-=x&-x)ans+=a[x];
        return ans;
    }
}t;

int line[N],li,ty[N];
bool vis[N];
int x,y,z,n;
char s[11];

int main(){
    cin>>n;
    while(n--){
        cin>>s;
        if(s[0]=='A'){
            vis[++li]=0;
            cin>>x>>y>>z;
            if(x==0){
                if(y>z) t.add(1,1),line[li]=1;
                else line[li]=2;
                ty[li]=-1;
            }
            else {
                if(x>0) line[li]=min((int)max(floor((double)(z-y)/x+1),-F+1.0),F)+F,t.add(line[li],1),ty[li]=1;
                else line[li]=min((int)max(ceil((double)(z-y)/x-1),-F+1.0),F)+F,t.add(1,1),t.add(line[li]+1,-1),ty[li]=0;
            }
        }
        else if(s[0]=='D'){
            cin>>x;
            if(!vis[x]){
                vis[x]=1;
                if(ty[x]==1) t.add(line[x],-1);
                else if(ty[x]==0) t.add(1,-1),t.add(line[x]+1,1);
                else if(ty[x]==-1&&line[x]==1) t.add(1,-1);
            }
        }
        else if(s[0]=='Q'){
            cin>>x;
            cout<<t.query(x+F)<<endl;
        }
    }
    return 0;
}