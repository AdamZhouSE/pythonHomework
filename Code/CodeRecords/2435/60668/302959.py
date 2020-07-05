#include <ctime>
#include <cmath>
#include <cstdio>
#include <string>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <algorithm>//头文件准备
#define in freopen (".in","r",stdin)
#define out freopen (".out","w",stdout)
#define INF 2147483647
#define UNINF -2147483648ll
#define ch char
#define bo bool
#define ui unsigned int
#define ll long long//闪现为了少打几个字符，弄了好多好多宏定义
using namespace std;

int n,m;
struct Name{
    string c,s;
    int id;
}name[50005];
inline bo cmp(Name x,Name y){
    return x.s>y.s;
}
inline void work();

int main(){
    //in;out;
    work();
    return 0;
}

inline void work(){
    scanf ("%d %d",&n,&m);
    string c1;
    for (int i=1;i<=n;i++){
        cin>>c1;
        int l=sizeof(c1);
        name[i].c=c1;
        for (int j=0;j<l;j++){
            if (c1[j]<='Z'&&c1[j]>='A')c1[j]=c1[j]-'A'+'a';
            else c1[j]=c1[j];
        }
        name[i].s=c1;
        name[i].id=i;
    }
    sort (name+1,name+1+n,cmp);
    for (int i=1,x,y;i<=m;i++){
        scanf ("%d %d",&x,&y);
        int j=1;
        while (1){
            if (name[j].id>=x&&name[j].id<=y)break;
            j++;
        }
        cout<<name[j].c<<endl;
    }
}