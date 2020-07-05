#include<iostream>
#include<cstdio>
#include<cstring>
#include<queue>
using namespace std;
string mob[300010];
int num[300010];
int ch[300010][26];
int fail[300010];
int ans[300010];
int temp;
int n,siz;
void insert(string s,int v){
    int now=0;
    for(int i=0;i<s.size();i++){
        int o=s[i]-'a';
        if(!ch[now][o])ch[now][o]=++siz;
        now=ch[now][o];
    }
    num[now]=v;
}
void getfail(){
    int now=0;
    queue<int>que;
    for(int i=0;i<26;i++)if(ch[0][i])que.push(ch[0][i]),fail[ch[0][i]]=0;
    while(!que.empty()){
        int u=que.front();que.pop();
        for(int i=0;i<26;i++){
            int v=ch[u][i];
            if(v)fail[v]=ch[fail[u]][i],que.push(v);
            else ch[u][i]=ch[fail[u]][i];
        }
    }
}
void query(string s){
    int now=0;
    for(int i=0;i<s.size();i++){
        now=ch[now][s[i]-'a'];
        for(int j=now;j;j=fail[j])ans[num[j]]++;
    }
}
int main(){
    while(cin>>n&&n){
        memset(num,0,sizeof(num));
        memset(ans,0,sizeof(ans));
        memset(ch,0,sizeof(ch));
        memset(fail,0,sizeof(fail));
        siz=0;
        for(int i=1;i<=n;i++){
            cin>>mob[i];
            insert(mob[i],i);
        }
        getfail();
        string k;
        cin>>k;
        query(k);
        temp=0;
        for(int i=1;i<=n;i++)if(ans[i]>temp)temp=ans[i];
        cout<<temp<<"\n";
        for(int i=1;i<=n;i++)if(ans[i]==temp)cout<<mob[i]<<"\n";
    }
}