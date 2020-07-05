#include<bits/stdc++.h>
#define ls s[x].son[0]
#define rs s[x].son[1]
using namespace std;
int n,t,a,b,c;
struct node{
    int dis,val,son[2],rt;
}s[150010];
int merge(int x,int y){
    if(!x||!y)return x+y;
    if(s[x].val>s[y].val||(s[x].val==s[y].val&&x>y))swap(x,y);
    rs=merge(rs,y);
    if(s[ls].dis<s[rs].dis)swap(ls,rs);
    s[ls].rt=s[rs].rt=s[x].rt=x;
    s[x].dis=s[rs].dis+1;
    return x;
}
int get(int x){
    if(s[x].rt==x)return x;
    s[x].rt=get(s[x].rt);
    return s[x].rt;
}
void pop(int x){
    s[x].val=-1;
    s[ls].rt=ls;
    s[rs].rt=rs;
    s[x].rt=merge(ls,rs);
}
int main(){
    cin>>n>>t;
    s[0].dis=-1;
    for(int i=1;i<=n;i++){
        s[i].rt=i;
        scanf("%d",&s[i].val);
    }
    for(int i=1;i<=t;i++){
        scanf("%d%d",&a,&b);
        if(a==1){
            scanf("%d",&c);
            if(s[b].val==-1||s[c].val==-1)continue;
            int B=get(b),C=get(c);
            if(B!=C){
                s[B].rt=s[C].rt=merge(B,C);
            }
        }else{
            if(s[b].val==-1)printf("-1\n");
            else printf("%d\n",s[get(b)].val),pop(get(b));
        }
    }
    return 0;
}