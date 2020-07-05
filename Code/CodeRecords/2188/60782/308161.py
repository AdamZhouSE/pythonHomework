#include <bits/stdc++.h>

using namespace std;

typedef long long lol;
typedef pair<int,int> pii;
const int N = 4e5 + 5;
const int LG = 19;
const int INF = 0x3f3f3f3f;
const int U = 261;
int _w;

char S[N] , T[N] , ST[N];
int n , len , Q , K; lol ans[N];

struct Query {
  int id , l , r , s , t , len;
  bool operator < ( const Query & rhs ) const {
    return len < rhs.len;
  }
} query[N];

namespace SA {
  int sa[N] , rnk[N] , ht[19][N] , kc[N] , tp[N] , c[N] , rt[N] , son[N << 5][2] , mn[N << 5] , Log[N] , nidx;
  bool cmp( int a , int b , int k ) { return tp[a] == tp[b] && tp[a + k] == tp[b + k]; }
  void up( int u ) { mn[u] = INF; if( son[u][0] ) mn[u] = min( mn[u] , mn[son[u][0]] ); if( son[u][1] ) mn[u] = min( mn[u] , mn[son[u][1]] ); }
  void ins( int l , int r , int & u , int v , int pos , int k ) {
    mn[u = ++nidx] = INF;
    if( l == r ) { mn[u] = min( mn[u] , k ); return; }
    int mid = ( l + r ) >> 1;
    if( mid >= pos ) ins( l , mid , son[u][0] , son[v][0] , pos , k ) , son[u][1] = son[v][1];
    else ins( mid + 1 , r , son[u][1] , son[v][1] , pos , k ) , son[u][0] = son[v][0];
    up( u );
  }
  int qry( int l , int r , int u , int L , int R ) {
    if( !u ) return INF;
    if( l >= L && r <= R ) return mn[u];
    int mid = ( l + r ) >> 1 , res = INF;
    if( mid >= L ) res = min( res , qry( l , mid , son[u][0] , L , R ) );
    if( mid < R ) res = min( res , qry( mid + 1 , r , son[u][1] , L , R ) );
    return res;
  }
  void SuffixSort( int m = 260 ) {
    static int i , p , k;
    for( i = 1 ; i <= len ; ++i ) ++c[rnk[i] = ST[i]];
    for( i = 1 ; i <= m ; ++i ) c[i] += c[i - 1];
    for( i = len ; i ; --i ) sa[c[ST[i]]--] = i;
    for( k = 1 , p = 0 ; p < len ; m = p , k <<= 1 ) {
      p = 0; for( i = len - k + 1 ; i <= len ; ++i ) tp[++p] = i;
      for( i = 1 ; i <= len ; ++i ) if( sa[i] > k ) tp[++p] = sa[i] - k;
      for( i = 0 ; i <= m ; ++i ) c[i] = 0;
      for( i = 1 ; i <= len ; ++i ) ++c[rnk[i]] , kc[i] = rnk[tp[i]];
      for( i = 1 ; i <= m ; ++i ) c[i] += c[i - 1];
      for( i = len ; i ; --i ) sa[c[kc[i]]--] = tp[i];
      for( i = 1 ; i <= len ; ++i ) swap( rnk[i] , tp[i] );
      rnk[sa[1]] = p = 1;
      for( i = 2 ; i <= len ; ++i ) rnk[sa[i]] = cmp( sa[i] , sa[i - 1] , k ) ? p : ++p;
    } for( i = 1 ; i <= len ; ++i ) rnk[sa[i]] = i;
    for( i = 1 , k = 0 ; i <= len ; ++i ) {
      p = sa[rnk[i] - 1];
      if( k ) --k;
      while( ST[i + k] == ST[p + k] ) ++k;
      ht[0][rnk[i]] = k;
    }
    for( k = 1 ; k < LG ; ++k )
      for( i = 1 , p = len - ( 1 << k ) + 1 ; i <= p ; ++i )
        ht[k][i] = min( ht[k - 1][i] , ht[k - 1][i + ( 1 << ( k - 1 ) )] );
    for( i = 2 ; i <= len ; ++i ) Log[i] = Log[i >> 1] + 1;
  }
  void init( void ) {
    SuffixSort();
    for( int i = n ; i ; --i ) {
      ins( 1 , len , rt[i] , rt[i + 1] , rnk[i] , i );
    }
  }
  int qry( int l , int r ) {
    static int k;
    if( l > r ) swap( l , r );
    k = Log[r - l]; ++l;
    return min( ht[k][l] , ht[k][r - ( 1 << k ) + 1] );
  }
  pii get( int s , int t ) {
    int p = rnk[s + n] , L = rnk[s + n] , R = rnk[s + n] , l , r , mid , res;
    t = t - s + 1;
    l = 1 , r = L - 1 , res = L;
    while( l <= r ) {
      mid = ( l + r ) >> 1;
      if( qry( mid , p ) >= t ) res = mid , r = mid - 1;
      else l = mid + 1;
    } L = res;
    l = R + 1 , r = len , res = R;
    while( l <= r ) {
      mid = ( l + r ) >> 1;
      if( qry( mid , p ) >= t ) res = mid , l = mid + 1;
      else r = mid - 1;
    } R = res;
    return pii( L , R );
  }
  lol qry( int l , int r , int s , int t ) {
    pii seg = get( s , t );
    lol res = 0; int now;
    while( l + ( t - s ) <= r ) {
      l = qry( 1 , len , rt[l] , seg.first , seg.second );
      if( l + ( t - s ) <= r )
        res += max( 0 , K - l );
      l += ( t - s ) + 1;
    }
    return res;
  }
}

int q[N] , nq[N] , id[N] , nid[N] , c[U] , head[N] , stk[N] , tp , eidx , ed[N] , mxlen; lol Sstk[N];
struct Edge { int nxt , to; } edge[N];
void addedge( int u , int v ) { edge[++eidx] = (Edge) { head[u] , v }; head[u] = eidx;}
bool cmp( int a , int b ) { return ST[a] == ST[b] && id[a + 1] == id[b + 1];}
vector<pii> qry[N];

void dfs( int u ) {
  if( u ) { stk[++tp] = u; Sstk[tp] = Sstk[tp - 1] + max(K-u,0); }
  for( int i = 0 , t = qry[u].size() , l , r , mid , res ; i < t ; ++i ) {
    pii tmp = qry[u][i];
    l = 1 , r = tp , res = 0;
    while( l <= r ) {
      mid = ( l + r ) >> 1;
      if( stk[mid] <= tmp.second ) res = mid , r = mid - 1;
      else l = mid + 1;
    } l = res , r = tp;
    ans[tmp.first] = ( Sstk[tp] - Sstk[res - 1] );
  }
  for( int i = head[u] ; i ; i = edge[i].nxt )
    dfs( edge[i].to );
  if( u ) --tp;
}

void put( int id , int L , int R , int s , int t ) {
  int l = ::id[s + n] , r = ed[l] , mid , res = r + 1;
  while( l <= r ) {
    mid = ( l + r ) >> 1;
    if( q[mid] >= L ) res = mid , r = mid - 1;
    else l = mid + 1;
  }
  if( q[res] + ( t - s ) <= R ) {
    qry[q[res]].push_back( pii( id , R - ( t - s ) ) );
  }
}

int main( void ) {
  _w = scanf("%d%d%s%s%d",&n,&K,S+1,T+1,&Q);
  for( int i = 1 ; i <= Q ; ++i ) {
    _w = scanf("%d%d%d%d",&query[i].l,&query[i].r,&query[i].s,&query[i].t);
    query[i].len = query[i].t - query[i].s + 1 , query[i].id = i;
    mxlen = max( mxlen , query[i].t - query[i].s + 1 );
  } sort( query + 1 , query + 1 + Q );
  memcpy( ST + 1 , S + 1 , sizeof( char ) * n );
  memcpy( ST + n + 1 , T + 1 , sizeof( char ) * n );
  len = n * 2;
  SA::init();
  for( int i = 1 ; i <= len + 1 ; ++i ) q[i] = i;
  for( int k = 1 , L = 1 , R , now , lk = min( 50 , mxlen ) ; k <= lk ; ++k , L = R + 1 ) {
    R = L - 1;
    while( R < Q && query[R + 1].len == k ) ++R;
    now = len - k + 1;
    for( int i = 0 ; i < U ; ++i ) c[i] = 0;
    for( int i = 1 ; i <= now ; ++i ) ++c[ST[i]];
    for( int i = 1 ; i < U ; ++i ) c[i] += c[i - 1];
    for( int i = now + 1 , x ; i ; --i ) {
      x = q[i] - 1;
      if( !x ) continue;
      nq[c[ST[x]]--] = x;
    }
    memset( head , 0 , sizeof( int ) * ( now + 1 ) ) , eidx = 0;
    for( int i = 0 ; i <= now ; ++i ) qry[i].clear();
    for( int i = 1 , r ; i <= now ; i = r + 1 ) {
      r = i;
      while( r < now && cmp( nq[r] , nq[r + 1] ) ) ++r;
      ed[i] = r;
      for( int j = i ; j <= r ; ++j ) nid[nq[j]] = i;
      for( int j = i , t = i ; j <= r ; ++j ) {
        while( t <= r && nq[t] - nq[j] < k ) ++t;
        addedge( t > r ? 0 : nq[t] , nq[j] );
      }
    }
    for( int i = 1 ; i <= now ; ++i ) q[i] = nq[i] , id[i] = nid[i];
    for( int i = L ; i <= R ; ++i ) put( query[i].id , query[i].l , query[i].r , query[i].s , query[i].t );
    if( R >= L ) dfs( 0 );
  }
  for( int i = 1 ; i <= Q ; ++i )
    if( query[i].len > 50 )
      ans[query[i].id] = SA::qry( query[i].l , query[i].r , query[i].s , query[i].t );
  for( int i = 1 ; i <= Q ; ++i )
    printf("%lld\n",ans[i]);
  return 0;
}