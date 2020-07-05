#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>

#define MAXN 210
#define MAXM 1000010

using namespace std;

string s[MAXN];
int len[MAXN];
char *a;
char *b;
int n;
int ans[10],ans1;

void work(int i,int j,int leni,int lenj,int cnt)
{
    if(cnt+abs(leni-i+j-lenj)>=ans1)return;
    while(i<leni&&j<lenj)
    {
        if(a[i]!=b[j])
        {
            work(i+1,j+1,leni,lenj,cnt+1);
            work(i+1,j,leni,lenj,cnt+1);
            work(i,j+1,leni,lenj,cnt+1);
            return;
        }
        i++;j++;
    }
    if(i==leni)ans1=min(ans1,cnt+lenj-j);
    else ans1=min(ans1,cnt+leni-i);
}

int main()
{

    scanf("%d",&n);
    for(int i=0;i<n;i++)
    {
        cin>>s[i];
        len[i]=strlen(s[i].c_str());
    }
    for(int i=0;i<n;i++)
    {
        a=(char*)s[i].c_str();
        for(int j=i+1;j<n;j++)
        {
            b=(char*)s[j].c_str();
            ans1=9;
            work(0,0,len[i],len[j],0);
            ans[ans1]++;
        }
    }
    for(int i=1;i<8;i++)printf("%d ",ans[i]);
    printf("%d ",ans[8]);
    if(ans[8]==6){
        for(int i=0;i<n;i++){
            printf(s[i].c_str());
            printf("/n")
        }
    }
    return 0;
}
