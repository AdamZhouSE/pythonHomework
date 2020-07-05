#include<stdio.h>
#include<string.h>
#include<iostream>
using namespace std;

char num[250];
bool vis[250] = {false};

void del(char num[],bool vis[])
{
    int i,j;
    int flag = 0;
    int len = strlen(num);
    for(i = 9;i>=0;i--)
    {

        for(j = 0;j<len;j++)
        {
            if(vis[j] == false && (num[j] - '0'==i))
            {
                flag = 1;
                vis[j] = true;
                break;
            }
        }

        if(flag == 1)
            return ;
    }
}

int main()
{
    int N;

    scanf("%s",num);
    scanf("%d",&N);
    int len = strlen(num);
    for(int i = 0;i<N;i++)
    {
        del(num,vis);
    }
    for(int j = 0;j<len;j++)
    {
        if(vis[j]==false)
            printf("%c",num[j]);
    }
    return 0;

}