#include<bits/stdc++.h>
using namespace std;
#define N 200020
int n,ans;
int len[30];
char s[N];
struct email{int l,r;};
vector<email>v[30][30];
bool cmp(email a,email b){return a.l>b.l;}
void pre()
{
    int i=1,j,l=1,r;char ml=s[1],mr;
    while(s[i]==s[i+1])i++,l++;
    while(i<n)
    {
        j=i+1;mr=s[j];r=1;
        while(j<n&&s[j]==s[j+1])j++,r++;
        v[ml-'a'][mr-'a'].push_back((email){l,r});
        i=j,l=r,ml=mr;
    }
}

inline void cal(int x,int y)
{
    sort(v[x][y].begin(),v[x][y].end(),cmp);
    int i=0;email p=v[x][y][i];
    int ml=p.l,mr=p.r;ans+=ml*mr;i++;
    for(;i<v[x][y].size();i++)
    {
        email p=v[x][y][i];
        if(mr<p.r)ans+=p.l*(p.r-mr),mr=p.r;
    }

}

int main()
{
    scanf("%s",s+1);n=strlen(s+1);
    for(int i=1;i<=n;)
    {
        int j=i;
        while(j<n&&s[j]==s[j+1])j++;
        len[s[i]-'a']=max(len[s[i]-'a'],j-i+1);
        i=j+1;
    }
    for(int i=0;i<26;i++)ans+=len[i];
    pre();
    for(int i=0;i<26;i++)
        for(int j=0;j<26;j++)
            if(v[i][j].size())
                cal(i,j);
    printf("%d\n",ans);
    return 0;
}