#include <cstdio>
#include <cstring>

typedef long long LL;

const int mod = 1e9 + 7;
const int MAXSIZ = 30, MAXLEN = 1e5 + 5;

template<typename _T>
void read( _T &x )
{
    x = 0;char s = getchar();int f = 1;
    while( s > '9' || s < '0' ){if( s == '-' ) f = -1; s = getchar();}
    while( s >= '0' && s <= '9' ){x = ( x << 3 ) + ( x << 1 ) + ( s - '0' ), s = getchar();}
    x *= f;
}

template<typename _T>
void write( _T x )
{
    if( x < 0 ){ putchar( '-' ); x = ( ~ x ) + 1; }
    if( 9 < x ){ write( x / 10 ); }
    putchar( x % 10 + '0' );
}

struct matrix
{
    int mat[MAXSIZ][MAXSIZ], n, m;
    matrix( const int N = 0, const int M = 0 ) { n = N, m = M, memset( mat, 0, sizeof mat ); }
    int * operator [] ( const int & indx ) { return mat[indx]; }
    matrix operator * ( matrix other ) const 
    {
        matrix ret = matrix( n, other.m );
        for( int i = 1 ; i <= ret.n ; i ++ )
            for( int j = 1 ; j <= ret.m ; j ++ )
                for( int k = 1 ; k <= m ; k ++ )
                    ret[i][k] = ( ret[i][k] + 1ll * mat[i][j] * other[j][k] % mod ) % mod;
        return ret;
    }
    void operator *= ( matrix other ) { *this = *this * other; }
}A, B;

LL N;
int M;
char S[MAXLEN];

int getIndx( char c ) { return c - 'a' + 1; }
matrix I( const int n ) 
{ matrix ret = matrix( n, n ); for( int i = 1 ; i <= n ; i ++ ) ret[i][i] = 1; return ret; }

matrix qkpow( matrix base, LL indx )
{
    matrix ret = I( base.n );
    while( indx )
    {
        if( indx & 1 ) ret *= base;
        base *= base; indx >>= 1;
    }
    return ret;
}

void init()
{
    A = matrix( 1, 26 );
    for( int i = 1 ; i <= 26 ; i ++ ) A[1][i] = 1;
    B = matrix( 26, 26 );
    for( int i = 1 ; i <= 26 ; i ++ )
        for( int j = 1 ; j <= 26 ; j ++ )
            B[i][j] = 1;
}

int main()
{
    init();
    read( N );
    scanf( "%s", S + 1 ), M = strlen( S + 1 );
    for( int i = 1 ; i < M ; i ++ ) B[getIndx( S[i] )][getIndx( S[i + 1] )] = 0;
    matrix part = qkpow( B, N - 1 );
    matrix fine = A * part;
    int res = 0;
    for( int i = 1 ; i <= 26 ; i ++ ) res = ( res + fine[1][i] ) % mod;
    write( res ), putchar( '\n' );
    return 0;
}