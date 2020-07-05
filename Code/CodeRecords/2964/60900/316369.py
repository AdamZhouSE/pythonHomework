#include <cmath>
#include <cstdio>
#include <string>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
int n,k,lena,lenb,tempans,ans[10];
char a[1000500],b[1000500];
string str[205];
void dfs(int solvedx,int solvedy,int dep){
    if(dep+abs((lena-solvedx)-(lenb-solvedy))>=tempans)return;
    while(a[solvedx]==b[solvedy]&&solvedx<lena&&solvedy<lenb)solvedx++,solvedy++;
    if(solvedx==lena){tempans=min(tempans,dep+lenb-solvedy);return;}
    if(solvedy==lenb){tempans=min(tempans,dep+lena-solvedx);return;}
    dfs(solvedx+1,solvedy+1,dep+1);
    dfs(solvedx+1,solvedy,dep+1);
    dfs(solvedx,solvedy+1,dep+1);
}
bool cmp(string &a,string &b){return a.size()>b.size();}
int main(){
    scanf("%d%d",&n,&k);
    for(int i=1;i<=n;i++)cin>>str[i];
    sort(str+1,str+1+n,cmp);
    for(int i=1;i<=n;i++){
        strcpy(a,str[i].c_str());
        lena=strlen(a);
        for(int j=i+1;j<=n;j++){
            if(abs((int)str[j].size()-(int)str[i].size())<9){
                strcpy(b,str[j].c_str());
                lenb=strlen(b);
                tempans=9;
                dfs(0,0,0);
                ans[tempans]++;
            }
        }
    }
    for(int i=1;i<=8;i++)printf("%d ",ans[i]);
}