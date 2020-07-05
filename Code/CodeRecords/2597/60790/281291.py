#include<bits/stdc++.h>
#define lol long long
#define il inline
#define rg register
#define Min(a,b) (a)<(b)?(a):(b)
#define Max(a,b) (a)>(b)?(a):(b)

using namespace std;

const int N=1e5+10;

void in(lol &ans)
{
    ans=0; lol f=1; char i=getchar();
    while(i<'0' || i>'9') {if(i=='-') f=-1; i=getchar();}
    while(i>='0' && i<='9') ans=(ans<<1)+(ans<<3)+i-'0', i=getchar();
    ans*=f;
}

struct node {
    lol x,v;
    bool operator < (const node & a) const {return v<a.v;}
};
set<node>v;

int main()
{
    lol op,x,y; node tmp;
    while(1) {
        in(op);
        if(op==1) {
            in(x),in(y);
            tmp = (node) {x,y};
            v.insert(tmp);
        }
        else if(op==2) {if(v.size()) v.erase(--v.end());}
        else if(op==3) {if(v.size()) v.erase(v.begin());}
        else {
            lol ans1=0,ans2=0;
            for(set<node>::iterator it=v.begin();it!=v.end();it++) ans1+=(*it).x,ans2+=(*it).v;
            printf("%lld %lld",ans1,ans2);
            return 0;
        }
    }
    return 0;
}