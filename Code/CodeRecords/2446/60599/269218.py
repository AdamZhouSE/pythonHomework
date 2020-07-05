#include<cstdio>
#include<iostream>
#include<algorithm>
#include <bitset>

using namespace std;

int n,m;
char s[1001];
int l;
int tot=0;
int tri[300007][26];
bitset<1001> b[500007];

inline void insert(char *s,int x){
    int rt=0;
    for(int i=0;s[i];i++){
        int v=s[i]-'a';
        if(!tri[rt][v]){
            tri[rt][v]=++tot;
        }
        rt=tri[rt][v];
    }
    b[rt][x]=1;
}

inline void query(char *s){
    int rt=0;
    for(int i=0;s[i];i++){
        int v=s[i]-'a';
        if(!tri[rt][v]){
            cout<<' '<<endl;
            return;
        }
        rt=tri[rt][v];
    }
    for(int i=1;i<=n;i++){
        if(b[rt][i]==1){
            cout<<i<<' ';
        }
    }
    cout<<endl;
}

int main(){
    cin>>n;
    for(int i=1;i<=n;i++){
        cin>>l;
        for(int j=1;j<=l;j++){
            cin>>s;
            insert(s,i);
        }
    }
    cin>>m;
    for(int i=1;i<=m;i++){
        cin>>s;
        query(s);
    }
    return 0;
}