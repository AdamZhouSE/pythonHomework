#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<string>
#include<algorithm>
using namespace std;
struct Node{
    int son[27],f,vis;
}N[500010];
int n,m,cnt=1;
char name[55];
void insert(char name[]){
    int now=1;
    for(int i=0;name[i]!='\0';i++){
        if(N[now].son[name[i]-'a']) now=N[now].son[name[i]-'a'];
        else{N[now].son[name[i]-'a']=++cnt; now=cnt;}
    }
    N[now].f=1;
}
int find(char name[]){
    int now=1;
    for(int i=0;name[i]!='\0';i++){
        if(!N[now].son[name[i]-'a']) return -1;
        else now=N[now].son[name[i]-'a'];
    }
    if(N[now].f){
        if(N[now].vis) return 0;
        else{
            N[now].vis=1;
            return 1;
        }
    }
    else return -1;
}
int main(){
    scanf("%d",&n);
    for(int i=1;i<=n;i++){
        scanf("%s",name);
        insert(name);
    }
    scanf("%d",&m);
    for(int i=1;i<=m;i++){
        scanf("%s",name);
        int pd=find(name);
        if(pd==-1) printf("WRONG\n");
        else if(pd==0) printf("REPEAT\n");
        else printf("OK\n");
    }
    return 0;
}


















































