namespace SA {
    int sa[N], rk[N], tp[N], tx[N];

    inline void tsort() {
        for (int i = 1; i <= m; i++) tx[i] = 0;
        for (int i = 1; i <= n; i++) ++tx[rk[i]];
        for (int i = 1; i <= m; i++) tx[i] += tx[i-1];
        for (int i = n; i; i--) sa[tx[rk[tp[i]]]--] = tp[i];
    }

    inline bool pd(int i, int w) {
        return tp[sa[i-1]] == tp[sa[i]] && tp[sa[i-1]+w] == tp[sa[i]+w];
    }

    inline void main() {
        for (int i = 1; i <= n; i++) rk[i] = s[i] - 'a' + 1, tp[i] = i;
        tsort();
        for (int w = 1, p = 0; p < n; w <<= 1, m = p) {
            p = 0;
            for (int i = 1; i <= w; i++) tp[++p] = n - w + i;
            for (int i = 1; i <= n; i++) if (sa[i] > w) tp[++p] = sa[i] - w;
            tsort(), swap(rk, tp), rk[sa[1]] = p = 1;
            for (int i = 2; i <= n; i++) rk[sa[i]] = pd(i, w) ? p : ++p;
        }
    }
}