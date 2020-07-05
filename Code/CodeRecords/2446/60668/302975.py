#include <cstdio>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <iostream>
using namespace std;
char s[10010];
int nex[500010][26],n,cnt=0;
bool b[500010][110];
inline int read()
{
    int k=0,f=1;char ch=getchar();
    while(ch<'0'||ch>'9')
    {
        if(ch=='-')
            f=-1;
        ch=getchar();
    }
    while(ch>='0'&&ch<='9')
    {
        k=k*10+ch-'0';
        ch=getchar();
    }
    return k*f;
}
inline void insert(int x)
{
    scanf("%s",s+1);
    int l=strlen(s+1);
    int now=0;
    for(int i=1;i<=l;i++)
    {
        int p=s[i]-'a';
        if(!nex[now][p])         //如果$Trie$树中没有这个单词的前缀就进行编号
            nex[now][p]=++cnt;   //上文中说到的编号 
        now=nex[now][p];         //接着深入一层，更新现在的位置 
    }
    b[now][x]=1;                 //这个单词在第x行出现了
}
inline void check()
{
    scanf("%s",s+1);
    int l=strlen(s+1);
    int now=0,flag=1;
    for(int i=1;i<=l;i++)
    {
        int p=s[i]-'a';
        if(!nex[now][p])         //如果在Trie树中没有当前的字符，就可以直接break掉了 
        {
            flag=0;
            break;
        }
        now=nex[now][p];         //否则就更新位置 
    }
    if(flag)
        for(int i=1;i<=n;i++)    //题面上说按字典序输出 
            if(b[now][i])
                printf("%d ",i); //输出在哪些句子中出现过 
    puts("");                    //相当于printf("\n");其实这个条件很容易看不到，一定要注意啊！！ 
}
int main()
{
    n=read();
    for(int i=1;i<=n;i++)
    {
        int x=read();
        for(int j=1;j<=x;j++)    //一个单词一个单词的插入Trie树里 
            insert(i);
    }
    int m=read();
    for(int i=1;i<=m;i++)
        check();
    return 0;
}