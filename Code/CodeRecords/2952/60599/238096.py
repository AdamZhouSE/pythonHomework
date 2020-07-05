
# include <bits/stdc++.h>

const int N = 100005 ;

int go [N] [26], fail [N], fa [N], ncnt ;
int pos [N] ;

char buf [N] ;

struct edge  {
    int to, nxt ;
} g [N << 1] ;

int head [N], ecnt ;

inline void add_edge ( int u, int v )  {
    g [++ ecnt] = ( edge )  {  v, head [u]  } ;  head [u] = ecnt ;
}

struct Q {
    int x, qid ;
} ;

std :: vector < Q > qry [N] ;

void Extend ( char* s )  {
    int cur ( 0 ), id ( 0 ) ;
    for ( char* pt = s ; *pt ; ++ pt )  {
        if ( *pt == 'P' )  {
            pos [++ id] = cur ;
            continue ;
        }
        if ( *pt == 'B' )  {
            cur = fa [cur] ;
            continue ;
        }
        int k = *pt - 'a' ;
        if ( ! go [cur] [k] )   go [cur] [k] = ++ ncnt, fa [ncnt] = cur ;
        cur = go [cur] [k] ;
    }
}

void Build_fail ( )  {
    std :: queue < int > q ;
    for ( int i = 0 ; i < 26 ; ++ i )
        if ( go [0] [i] )  q.push ( go [0] [i]) ;
    while ( ! q.empty ( ) )  {
        int cur = q.front ( ) ;  q.pop ( ) ;
        for ( int i = 0 ; i ^ 26 ; ++ i )  {
            if ( go [cur] [i] )  {
                q.push ( go [cur] [i] ) ;
                fail [go [cur] [i]] = go [fail [cur]] [i] ;
            }  else  go [cur] [i] = go [fail [cur]] [i] ;
        }
    }
}

int in [N], out [N], idx ;

void Dfs ( int u )  {
    in [u] = ++ idx ;
    for ( int i = head [u] ; i ; i = g [i].nxt )
        Dfs ( g [i].to ) ;
    out [u] = ++ idx ;
}

int c [N << 1], rt ;

inline void Modify ( int pos, int delta )  {
    while ( pos <= idx ) c [pos] += delta, pos += pos & -pos ;
}

inline int Query ( int pos )  {
    for ( rt = 0 ; pos ; pos -= pos & -pos )    rt += c [pos] ;
    return rt ;
}

int ans [N] ;

int main ( )  {
    scanf ( "%s", buf ) ;
    Extend ( buf ) ;
    Build_fail ( ) ;
    for ( int i = 1 ; i <= ncnt ; ++ i ) add_edge ( fail [i], i ) ;
    Dfs ( 0 ) ;
    int n ;
    scanf ( "%d", & n ) ;
    for ( int i = 1 ; i <= n ; ++ i )  {
        int x, y ;  // x in y ;
        scanf ( "%d%d", & x, & y ) ;
        qry [y].push_back ( ( Q ) { x, i } ) ;
    }
    int cur ( 0 ), id ( 0 ) ;
    for ( char* pt = buf ; *pt ; ++ pt )  {
        if ( *pt == 'P' )  {
            int scnt = qry [++ id].size ( ) ;
            for ( int i = 0 ; i < scnt ; ++ i )  {
                int x = pos [qry [id] [i].x], qid = qry [id] [i].qid ;
                ans [qid] = Query ( out [x] ) - Query ( in [x] - 1 ) ;
            }
            continue ;
        }
        if ( *pt == 'B' )  {
            Modify ( in [cur], -1 ) ;
            cur = fa [cur] ;
            continue ;
        }
        cur = go [cur] [*pt - 'a'] ;
        Modify ( in [cur], 1 ) ;
    }
    for ( int i = 1 ; i <= n ; ++ i )  {
        printf ( "%d\n", ans [i] ) ;
    }
}