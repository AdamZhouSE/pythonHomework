#include <bits/stdc++.h>
using namespace std;
const int N = 100000;

int n, m, pos, a[N];

struct tModify {
    int type, l, r;
} mdf[N];

struct tData {
    int sum_0, sum_1;
    tData() { sum_0 = sum_1 = 0; }
    tData( int _sum_0, int _sum_1 ) { sum_0 = _sum_0; sum_1 = _sum_1; }

    tData operator + ( const tData &rhs ) const {
        return ( tData ) { sum_0 + rhs.sum_0, sum_1 + rhs.sum_1 };
    }
} now;

struct segment_tree {
    int sum[2][N<<2], opt[N<<2];  
    #define lson (o<<1)
    #define rson (o<<1|1)
    inline void pushup( int o, int l, int r ) {
        sum[0][o] = sum[0][lson] + sum[0][rson];
        sum[1][o] = sum[1][lson] + sum[1][rson];

        assert( sum[0][o] + sum[1][o] == r - l + 1 );
    }
    #define pushup( o ) pushup( o, l, r )
    inline void pushdown( int o, int l, int r )
    {
        if( opt[o] == -1 ) return;
        int mid = l + r >> 1, tp = opt[o];

        sum[tp][lson] = mid - l + 1; 
        sum[tp][rson] = r - mid;
        sum[tp^1][lson] = sum[tp^1][rson] = 0;
        opt[lson] = opt[rson] = tp;
        opt[o] = -1;
    }
    inline void build( int o, int l, int r, int val )
    {
        opt[o] = -1;
        if( l == r ) {
            sum[a[l]>=val][o] = 1, sum[a[l]<val][o] = 0; return;
            // if( a[l] >= val ) --> 1, else --> 0
        }
        int mid = l + r >> 1;

        build( lson, l, mid, val );
        build( rson,mid+1,r, val );
        pushup( o );
    }
    inline tData query( int o, int l, int r, int ql, int qr ) 
    {   
        if( ql <= l && r <= qr ) return ( tData ) { sum[0][o], sum[1][o] };
        pushdown( o, l, r ); int mid = l + r >> 1; tData ret;

        if( ql <= mid ) ret = ret + query( lson, l, mid, ql, qr );
        if( mid+1<=qr ) ret = ret + query( rson,mid+1,r, ql, qr );
        pushup( o );
        return ret;
    }
    inline void modify_up( int o, int l, int r, int ql, int qr )
    {
        pushdown( o, l, r );
        int mid = l + r >> 1, len = r - l + 1;
        if( ql <= l && r <= qr ) 
        {
            if( now.sum_0 >= len ) {
                sum[0][o] = len, sum[1][o] = 0, opt[o] = 0, now.sum_0 -= len; return;
            }
            if( !now.sum_0 ) {
                sum[1][o] = len, sum[0][o] = 0, opt[o] = 1, now.sum_1 -= len; return;
            }

            modify_up( lson, l, mid, ql, qr );
            modify_up( rson,mid+1,r, ql, qr );
            pushup( o ); return;
        }

        if( ql <= mid ) modify_up( lson, l, mid, ql, qr );
        if( mid+1<=qr ) modify_up( rson,mid+1,r, ql, qr );
        pushup( o );
    }
    inline void modify_down( int o, int l, int r, int ql, int qr ) 
    {
        pushdown( o, l, r );
        int mid = l + r >> 1, len = r - l + 1;
        if( ql <= l && r <= qr ) 
        {
            if( now.sum_1 >= len ) {
                sum[1][o] = len, sum[0][o] = 0, opt[o] = 1, now.sum_1 -= len; return;
            }
            if( !now.sum_1 ) {
                sum[0][o] = len, sum[1][o] = 0, opt[o] = 0, now.sum_0 -= len; return;
            }

            modify_down( lson, l, mid, ql, qr );
            modify_down( rson,mid+1,r, ql, qr );
            pushup( o ); return;
        }

        if( ql <= mid ) modify_down( lson, l, mid, ql, qr );
        if( mid+1<=qr ) modify_down( rson,mid+1,r, ql, qr );
        pushup( o );
    }
    inline void print( int o, int l, int r )
    {
        if( l == r ) {
            printf( "%d ", sum[1][o] == 1 ); return;
        }
        int mid = l + r >> 1; pushdown( o, l, r );

        print( lson, l, mid );
        print( rson,mid+1,r );
        pushup( o );
    }
    #undef lson
    #undef rson
} seg;

tData tmp; int ans;

inline bool check( int val )
{
    seg.build( 1, 1, n, val );
//  seg.print( 1, 1, n ); printf( "\n" );
    for( int i = 1; i <= m; i ++ )
    {
        now = seg.query( 1, 1, n, mdf[i].l, mdf[i].r );
        if( mdf[i].type )
            seg.modify_down( 1, 1, n, mdf[i].l, mdf[i].r );
        else seg.modify_up( 1, 1, n, mdf[i].l, mdf[i].r );
    }

//  seg.print( 1, 1, n ); printf( "\nval:%d\n",val ); 

    now = seg.query( 1, 1, n, pos, pos );
//    printf( "val:%d, tmp:%d %d\n", val, now.sum_0, now.sum_1 );
    return now.sum_1 == 1;
}

void solve( int l, int r )
{
    if( l > r ) return;

    int mid = l + r >> 1;
    bool b = check( mid );

    if( b ) {
        ans = mid; solve( mid+1, r );
    }
    else solve( l, mid-1 );
}

int main()
{
//  freopen( "sort4.in", "r", stdin );

    scanf( "%d%d", &n, &m );
    for( int i = 1; i <= n; i ++ )
        scanf( "%d", &a[i] );

    for( int i = 1; i <= m; i ++ )
        scanf( "%d%d%d", &mdf[i].type, &mdf[i].l, &mdf[i].r );

    scanf( "%d", &pos );

    solve( 1, n );

    printf( "%d\n", ans );

    return 0;
}