#include <stdio.h>
#include <string.h>
#define rep(i,st,ed) for (int i=st;i<=ed;++i)
#define copy(x,t) memcpy(x,t,sizeof(x))

typedef long long LL;
const int N=800005;

int queue[N],d[N];
int rec[N][26],tot=1,last=1;
int len[N],fa[N];
int cnt[N],rank[N];
int size[N][2];

char str1[N],str2[N];

void extend(int ch) {
    int p,q,np,nq;
    p=last; last=np=++tot; len[np]=len[p]+1;
    while (p&&!rec[p][ch]) {
        rec[p][ch]=np;
        p=fa[p];
    }
    if (!p) fa[np]=1;
    else {
        q=rec[p][ch];
        if (len[q]==len[p]+1) {
            fa[np]=q;
        } else {
            nq=++tot; len[nq]=len[p]+1;
            copy(rec[nq],rec[q]);
            fa[nq]=fa[q];
            fa[np]=fa[q]=nq;
            while (p&&rec[p][ch]==q) {
                rec[p][ch]=nq;
                p=fa[p];
            }
        }
    }
}

void solve() {
    int head=1,tail=0;
    rep(i,1,tot) d[fa[i]]++;
    rep(i,1,tot) if (!d[i]) queue[++tail]=i;
    while (head<=tail) {
        int now=queue[head++];
        size[fa[now]][0]+=size[now][0];
        size[fa[now]][1]+=size[now][1];
        if (!(--d[fa[now]])) queue[++tail]=fa[now];
    }
    LL ans=0;
    rep(i,1,tot) if (fa[i]) ans+=(LL)(len[i]-len[fa[i]])*size[i][0]*size[i][1];
    printf("%lld", ans);
}

int main(void) {
    scanf("%s",str1+1);
    scanf("%s",str2+1);
    int len1=strlen(str1+1);
    int len2=strlen(str2+1);
    int now=1; last=1;
    rep(i,1,len1) {
        extend(str1[i]-'a');
        now=rec[now][str1[i]-'a'];
        size[now][0]++;
    }
    now=last=1;
    rep(i,1,len2) {
        extend(str2[i]-'a');
        now=rec[now][str2[i]-'a'];
        size[now][1]++;
    }
    solve();
    return 0;
}
