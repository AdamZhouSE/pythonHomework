#include <cstdio>
#include <cstring>
#include <queue>
#define N 6000
#define M 300000
using namespace std;
int map[60][60] , mp[1000][1000], bx[60][60] , by[60][60] , tx , ty , head[N] , to[M] , val[M] , next[M] , cnt = 1 , s , t , dis[N] , frm[N];
char str[60];
bool vis[N];
bool bfs(int x)
{
	for(int i = 1; i <= ty ; ++i)
	{
		if(!mp[x][i] || vis[i]) continue;
		vis[i] = 1;
		if(!frm[i] || bfs(frm[i])) {
			frm[i] = x;
			return true;
		}
	}
	return false;
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
    for(i = 1 ; i <= n ; i ++ )
        for(j = 1 ; j <= m ; j ++ )
            if(!map[i][j])
                mp[bx[i][j]][by[i][j]] = 1;
    for(int i = 1; i <= tx ; ++i)
    {
    	memset(vis,0,sizeof(vis));
    	if(bfs(i)) ++ans;
	}
    printf("%d" , ans);
    return 0;
}