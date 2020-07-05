#include <cstdio>
#include <cstring>
#define ll int
#define inf 1<<30
#define mt(x,y) memset(x,y,sizeof(x))
#define il inline 
il ll max(ll x,ll y){return x>y?x:y;}
il ll min(ll x,ll y){return x<y?x:y;}
il ll abs(ll x){return x>0?x:-x;}
il void swap(ll &x,ll &y){ll t=x;x=y;y=t;}
il void read(ll &x){//快读 
    x=0;ll f=1;char c=getchar();
    while(c<'0'||c>'9'){if(c=='-')f=-f;c=getchar();}
    while(c>='0'&&c<='9'){x=x*10+c-'0';c=getchar();}
    x*=f;
}
using namespace std;
#define N 500010
struct Trie{
    ll val[N],ch[N][26],sz;
    Trie(){
        sz=1;
        memset(ch[0],0,sizeof(ch[0]));
        memset(val,0,sizeof(val));
    }//初始化 
    ll idx(char c){return c-'a';}
    void insert(char *s){
        ll u=0,len=strlen(s+1);
        for(ll i=1;i<=len;i++){
            ll c=idx(s[i]);
            if(!ch[u][c]){
                memset(ch[sz],0,sizeof(ch[sz]));
//              val[sz]=0;  这里并不需要这么标记中间信息，因为在初始化那里已经将所有的附加信息初始化为0了 
                ch[u][c]=sz++;
            }
            u=ch[u][c];
        }
    }
    ll search(char *s){
        ll u=0,len=strlen(s+1);
        for(ll i=1;i<=len;i++){
            ll c=idx(s[i]);
            if(!ch[u][c])return 0;
            //如果没有这个节点，也就意味着询问的这个字符串不存在，输出WRONG 
            u=ch[u][c];
        }
        if(!val[u]){
            val[u]=1;return 1;//这个字符串已经询问过了，标识一下，然后输出OK 
        }
        return 2;//这个字符串正确，但不是第一次出现，输出REPEAT 
    }
}tree;
ll n,m;
int main(){
    read(n);char s[100];
    for(ll i=1;i<=n;i++){
        scanf("%s",s+1);
        tree.insert(s);
    }
    read(m);
    for(ll i=1;i<=m;i++){
        scanf("%s",s+1);
        ll pd=tree.search(s);
        if(pd==0)printf("WRONG\n");
        else if(pd==1)printf("OK\n");
        else if(pd==2)printf("REPEAT\n");
    }
    return 0;
}