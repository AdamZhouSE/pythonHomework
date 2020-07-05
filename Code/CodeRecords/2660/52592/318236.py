#include<cstdio>
using namespace std;
const int R=1e5,N=(R+1)*20;
int n,m,now,sz,root[R+1],ls[N],rs[N],len[N];
char s[N];
inline int read(){
    int x=0,f=1;char ch=getchar();
    while(ch<'0'||ch>'9'){if(ch=='-')f=-1;ch=getchar();}
    while(ch>='0'&&ch<='9'){x=x*10+ch-'0';ch=getchar();}
    return x*f;
}
void insert(int &k,int last,int l,int r,int pos,int c){
    k=++sz;
    if(l==r){s[k]=c;return ;}
    ls[k]=ls[last];
    rs[k]=rs[last];
    int mid=l+r>>1;
    if(pos<=mid) insert(ls[k],ls[last],l,mid,pos,c);
    else insert(rs[k],rs[last],mid+1,r,pos,c);
}
void query(int &k,int last,int l,int r,int pos){
    if(l==r){putchar(s[k]);putchar('\n');return ;}
    int mid=l+r>>1;
    if(pos<=mid) query(ls[k],ls[last],l,mid,pos);
    else query(rs[k],rs[last],mid+1,r,pos);
}
int main(){
    n=read();
    for(int i=1,x;i<=n;i++){
        char op=0,ch=0;
        for(;op<'A'||op>'Z';op=getchar());
        if(op=='T'){
            for(;ch<'a'||ch>'z';ch=getchar());
            now++;
            len[now]=len[now-1]+1;
            insert(root[now],root[now-1],1,R,len[now],ch);
        }
        else if(op=='U'){
            x=read();
            now++;
            root[now]=root[now-x-1];
            len[now]=len[now-x-1];
        }
        else x=read(),query(root[now],root[now-1],1,R,x);
    }
    return 0;
} 