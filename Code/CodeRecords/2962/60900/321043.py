
#include <bits/stdc++.h>
using namespace std;
int vis[2000];
int res[510];
char str[2000][9];
int Transform(char key[])
{
    int val, a, b, c, len = strlen(key);
    a = b = c = 0;
    if(len >= 1)
       a = key[len - 1] - 'A';
    if(len >= 2)
       b = key[len - 2] - 'A';
    if(len >= 3)
       c = key[len - 3] - 'A';
    val = a + b * 32 + c * 32 * 32;
    return val;
}
int GetPt(char key[9], int p)
{
    int hashval = Transform(key) % p;
    if(vis[hashval] == 0 || strcmp(str[hashval], key) == 0)
    {
        vis[hashval] = 1;
        strcpy(str[hashval], key);
    }
    else
    {
        for(int i = 1; ; i++)
        {
            if(hashval + i * i < p)
            {
                 if(vis[hashval + i * i] == 0 || strcmp(str[hashval + i * i], key) == 0)
                {
                vis[hashval + i * i] = 1;
                hashval += i * i;
                strcpy(str[hashval], key);
                break;
                }
            }
            else
            {
                int temp = (hashval + i * i) % p;
                if(vis[temp] == 0 || strcmp(str[temp], key) == 0)
                {
                   vis[temp] = 1;
                   hashval = temp;
                   strcpy(str[hashval], key);
                   break;
                }
            }
            if(hashval - i * i >= 0)
            {
                if(vis[hashval - i * i] == 0 || strcmp(str[hashval - i * i], key) == 0)
                {
                    vis[hashval - i * i] = 1;
                    hashval -= i * i;
                    strcpy(str[hashval], key);
                    break;
                }
            }
            else
            {
                int temp = (hashval - i * i) % p + p;
                if(vis[temp] == 0 || strcmp(str[temp], key) == 0)
                {
                   vis[temp] = 1;
                   hashval = temp;
                   strcpy(str[hashval], key);
                   break;
                }
            }
 
        }
    }
    return hashval;
}
int main()
{
    int N, P, val;
    char key[9];
    scanf("%d %d", &N, &P);
    for(int i = 0; i < P; ++i)
        vis[i] = 0;
    for(int i = 1; i <= N; ++i)
    {
        if(i != 1)
            getchar();
        scanf("%s", key);
        res[i] = GetPt(key, P);
    }
    if(N > 0)
     printf("%d", res[1]);
    for(int i = 2; i <= N; ++i)
        printf(" %d", res[i]);
    cout<<endl;
}