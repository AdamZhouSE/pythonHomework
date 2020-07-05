#include<bits/stdc++.h>
using namespace std;
#define re register
#define ll long long
#define get getchar()
#define in inline
int p1,p2,p3;
char s[1000010];
int main()
{
    cin>>p1>>p2>>p3;
    scanf("%s",s+1);
    int n=strlen(s+1);
    for(re int i=1;i<=n;i++)
    {
        if(s[i]=='-'&&((s[i-1]<='9'&&s[i-1]>='0'&&s[i+1]<='9'&&s[i+1]>='0')||s[i-1]<='z'&&s[i+1]<='z'&&s[i-1]>='a'&&s[i+1]>='a'))//判断减号旁边的两个字符是否为同一类型
        {
            if(s[i-1]>=s[i+1])
            {
                putchar('-');
                continue;
            }//是否合法
            if(p3==2) //倒着输出
            {
                for(re int j=s[i+1]-1;j>s[i-1];j--)
                {
                    if(p1==3)
                    {
                        for(re int k=1;k<=p2;k++)putchar('*');
                        continue;
                    }
                    if(p1==1||(s[i-1]<='9'&&s[i-1]>='0'))
                    {
                        for(re int k=1;k<=p2;k++)putchar(char(j));
                    }
                    else
                    {
                        for(re int k=1;k<=p2;k++)putchar(char(j-('a'-'A')));
                    }
                }
            }
            else //正着输出
            {
                for(re int j=s[i-1]+1;j<s[i+1];j++)
                {
                    if(p1==3)
                    {
                        for(re int k=1;k<=p2;k++)putchar('*');
                        continue;
                    }
                    if(p1==1||(s[i-1]<='9'&&s[i-1]>='0'))
                    {
                        for(re int k=1;k<=p2;k++)putchar(char(j));
                    }
                    else
                    {
                        for(re int k=1;k<=p2;k++)putchar(char(j-'a'+'A'));
                    }
                }
            }
            continue;
        }
        putchar(s[i]);
    }
    printf("\n");
}