#include <cstdio>
#include <cstring>
#include <queue>
#define N 6000
#define M 300000
using namespace std;
queue<int> q;
int map[60][60] , bx[60][60] , by[60][60] , tx , ty , head[N] , to[M] , val[M] , next[M] , cnt = 1 , s , t , dis[N];
char str[60];
void add(int x , int y , int z)
{
    to[++cnt] = y , val[cnt] = z , next[cnt] = head[x] , head[x] = cnt;
    to[++cnt] = x , val[cnt] = 0 , next[cnt] = head[y] , head[y] = cnt;
}
bool bfs()
{
    int x , i;
    memset(dis , 0 , sizeof(dis));
    while(!q.empty()) q.pop();
    dis[s] = 1 , q.push(s);
    while(!q.empty())
    {
        x = q.front() , q.pop();
        for(i = head[x] ; i ; i = next[i])
        {
            if(val[i] && !dis[to[i]])
            {
                dis[to[i]] = dis[x] + 1;
                if(to[i] == t) return 1;
                q.push(to[i]);
            }
        }
    }
    return 0;
}
int dinic(int x , int low)
{
    if(x == t) return low;
    int temp = low , i , k;
    for(i = head[x] ; i ; i = next[i])
    {
        if(val[i] && dis[to[i]] == dis[x] + 1)
        {
            k = dinic(to[i] , min(temp , val[i]));
            if(!k) dis[to[i]] = 0;
            val[i] -= k , val[i ^ 1] += k;
            if(!(temp -= k)) break;
        }
    }
    return low - temp;
}
int main()
{
    int n , m , i , j , ans = 0;
    scanf("%d%d" , &n , &m);
    for(i = 1 ; i <= n ; i ++ )
    {
        scanf("%s" , str + 1);
        for(j = 1 ; j <= m ; j ++ )
            map[i][j] = (str[j] == '*' ? 0 : str[j] == 'x' ? 1 : 2);
    }
    for(i = 1 ; i <= n ; i ++ )
    {
        tx ++ ;
        for(j = 1 ; j <= m ; j ++ )
        {
            bx[i][j] = tx;
            if(map[i][j] == 2) tx ++ ;
        }
    }
    for(j = 1 ; j <= m ; j ++ )
    {
        ty ++ ;
        for(i = 1 ; i <= n ; i ++ )
        {
            by[i][j] = ty;
            if(map[i][j] == 2) ty ++ ;
        }
    }
    s = 0 , t = tx + ty + 1;
    for(i = 1 ; i <= tx ; i ++ ) add(s , i , 1);
    for(i = 1 ; i <= ty ; i ++ ) add(i + tx , t , 1);
    for(i = 1 ; i <= n ; i ++ )
        for(j = 1 ; j <= m ; j ++ )
            if(!map[i][j])
                add(bx[i][j] , by[i][j] + tx , 1);
    while(bfs()) ans += dinic(s , 1 << 30);
    printf("%d" , ans);
    return 0;
}