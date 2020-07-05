#include<bits/stdc++.h>
const int maxn = 200035;

int n,lim,sum[maxn],size[maxn],cnt[maxn],pos[maxn];
long long ans;
struct SAM
{
    int ch[maxn][27],fa[maxn],len[maxn],mx[maxn],lst,tot;
    void init()
    {
        lst = tot = 1;
    }
    void extend(int c, int v)
    {
        int p = lst, np = ++tot;
        lst = np, len[np] = len[p]+1, mx[np] = v;        //len[p+1]    Here　　居然打成标红的这个
        for (; p&&!ch[p][c]; p=fa[p]) ch[p][c] = np;
        if (!p) fa[np] = 1;
        else{
            int q = ch[p][c];
            if (len[p]+1==len[q]) fa[np] = q;
            else{
                int nq = ++tot;
                len[nq] = len[p]+1, mx[nq] = mx[q];
                memcpy(ch[nq], ch[q], sizeof ch[q]);
                fa[nq] = fa[q], fa[q] = fa[np] = nq;
                for (; p&&ch[p][c]==q; p=fa[p])
                    ch[p][c] = nq;
            }
        }
    }
    void calc()
    {
        for (int i=1; i<=tot; i++) ++cnt[len[i]];
        for (int i=1; i<=tot; i++) cnt[i] += cnt[i-1];
        for (int i=1; i<=tot; i++) pos[cnt[len[i]]] = i, --cnt[len[i]];
        for (int i=tot; i; i--)
        {
            int p = pos[i];
            mx[fa[p]] = std::max(mx[fa[p]], mx[p]); 
            ans += std::max(std::min(mx[p], len[p])-len[fa[p]], 0);
        }
    }
}f;
char s[maxn],t[maxn];

int main()
{
     scanf("%s%s%d",s+1,t+1,&lim);
     n = strlen(s+1);
     f.init();
     for (int i=1, j=0; i<=n; i++)
     {
        sum[i] = (t[i]=='0')+sum[i-1];
        while (sum[i]-sum[j] > lim) ++j;
        f.extend(s[i]-'a'+1, i-j);
     }
     f.calc();
     printf("%lld\n",ans);
     return 0;
}