#include<iostream>

#include<algorithm>

#include<set>

#define ll long long

using namespace std;

const int N=1e5+10;

int n,m,a[N];

ll val[N],cal2[N],t[N],tot[N],t2[N],val2[N];

set<int> s,s1;

int read() {int x;scanf("%d",&x);return x;}

ll calc(int L,int R) {return 1ll*((L+1)/2)*((R+2)/2)+1ll*((L+2)/2)*((R+1)/2);}

ll calc2(int L,int R)

{

    ll res=1ll*(L+1)*(R+1)-1;

    if(L) res--;if(R) res--;

    return max(0ll,res);

}

void add1(int x,ll k) {while(x<=n) t[x]+=k,x+=x&(-x);}

ll query1(int x) {ll s=0;while(x) s+=t[x],x-=x&(-x);return s;}

void add2(int x,ll k) {while(x<=n) t2[x]+=k,x+=x&(-x);}

ll query2(int x) {ll s=0;while(x) s+=t2[x],x-=x&(-x);return s;}

void WorkQ()

{

    int l,r,len;ll ans=0;

    scanf("%d%d",&l,&r);len=r-l+1;

    int pl=*s.lower_bound(l);

    int pr=*(--s.upper_bound(r));

    if(pl>r) return (void)printf("%lld\n",tot[len]-cal2[r-l+1]);

    if(pl==pr) return (void)printf("%lld\n",tot[len]-calc(pl-l,r-pl)-cal2[pl-l]-cal2[r-pr]);

    ans=query1(pr-1)-query1(pl);

    int d1=*s.upper_bound(pl)-pl-1;ans+=calc(pl-l,d1)+cal2[pl-l];

    int d2=pr-*(--s.lower_bound(pr))-1;ans+=calc(d2,r-pr)+cal2[r-pr];

    pl=*s1.lower_bound(l);

    pr=*(--s1.upper_bound(r));

    if(pl==pr) ans+=calc2(pl-l,r-pr);

    if(pl<pr)

    {

        d1=*s1.upper_bound(pl)-pl-1;ans+=calc2(pl-l,d1);

        d2=pr-*(--s1.lower_bound(pr))-1;ans+=calc2(d2,r-pr);

        ans+=query2(pr-1)-query2(pl);

    }

    printf("%lld\n",tot[len]-ans);

}

void WorkM()

{

    int p=read();a[p]^=1;

    if(a[p]==0)//1->0

    {

        s.insert(p);s1.erase(p);

        set<int>::iterator fr,nt,ffr,nnt;

        fr=s.lower_bound(p);fr--;

        nt=s.upper_bound(p);

        add1(p,-val[p]);

        add1(p,val[p]=calc(p-*fr-1,*nt-p-1));

        if(*fr!=0)

        {

            ffr=fr;ffr--;

            add1(*fr,-val[*fr]);

            add1(*fr,val[*fr]=calc(*fr-*ffr-1,p-*fr-1));

        }

        if(*nt!=n+1)

        {

            nnt=nt;nnt++;

            add1(*nt,-val[*nt]);

            add1(*nt,val[*nt]=calc(*nt-p-1,*nnt-*nt-1));

        }

        if(*nt-p-1>0)

        {

            add1(*nt-1,-val[*nt-1]);

            add1(*nt-1,val[*nt-1]=cal2[*nt-p-1]);

        }

        if(p-*fr-1>0)

        {

            add1(p-1,-val[p-1]);

            add1(p-1,val[p-1]=cal2[p-*fr-1]);

        }

        fr=s1.lower_bound(p);fr--;

        nt=s1.upper_bound(p);

        add2(p,-val2[p]),val2[p]=0;

        if(*fr!=0)

        {

            ffr=fr;ffr--;

            add2(*fr,-val2[*fr]);

            add2(*fr,val2[*fr]=calc2(*fr-*ffr-1,*nt-*fr-1));

        }

        if(*nt!=n+1)

        {

            nnt=nt;nnt++;

            add2(*nt,-val2[*nt]);

            add2(*nt,val2[*nt]=calc2(*nt-*fr-1,*nnt-*nt-1));

        }

    }

    else//0->1

    {

        s.erase(p);s1.insert(p);

        set<int>::iterator fr,nt,ffr,nnt;

        fr=s.upper_bound(p);nt=fr;fr--;

        if(*fr!=0)

        {           

            ffr=fr;ffr--;

            add1(*fr,-val[*fr]);

            add1(*fr,val[*fr]=calc(*fr-*ffr-1,*nt-*fr-1));

        }

        if(*nt!=n+1)

        {

            nnt=nt;nnt++;

            add1(*nt,-val[*nt]);

            add1(*nt,val[*nt]=calc(*nt-*fr-1,*nnt-*nt-1));

        }       

        if(*nt-p-1>0) add1(*nt-1,-val[*nt-1]),val[*nt-1]=0;

        if(p-*fr-1>0) add1(p-1,-val[p-1]),val[p-1]=0;

        add1(p,-val[p]),val[p]=0;

        add1(*nt-1,val[*nt-1]=cal2[*nt-*fr-1]);

        fr=s1.lower_bound(p);fr--;

        nt=s1.upper_bound(p);

        add2(p,-val2[p]);

        add2(p,val2[p]=calc2(p-*fr-1,*nt-p-1));

        if(*fr!=0)

        {

            ffr=fr;ffr--;

            add2(*fr,-val2[*fr]);

            add2(*fr,val2[*fr]=calc2(*fr-*ffr-1,p-*fr-1));

        }

        if(*nt!=n+1)

        {

            nnt=nt;nnt++;

            add2(*nt,-val2[*nt]);

            add2(*nt,val2[*nt]=calc2(*nt-p-1,*nnt-*nt-1));

        }

    }

}

int main()

{

    cin>>n;

    s.insert(0);s.insert(n+1);s1.insert(0);s1.insert(n+1);

    for(int i=1;i<=n;i++) a[i]=read(),a[i]?s1.insert(i):s.insert(i);

    for(int i=1;i<=n;i++) cal2[i]=(i&1)?(i+1)/2:cal2[i-1];

    for(int i=1;i<=n;i++) cal2[i]+=cal2[i-1];

    for(int i=1;i<=n;i++) tot[i]=tot[i-1]+i;

    set<int>::iterator it=s.begin(),fr,nt;

    for(;it!=s.end();it++)

    {

        if(*it==n+1)

        {

            fr=it,fr--;

            if(*it-*fr-1>0) add1(*it-1,val[*it-1]=cal2[*it-*fr-1]);

        }

        if(*it==0||*it==n+1) continue;

        fr=nt=it;fr--,nt++;

        add1(*it,val[*it]=calc(*it-*fr-1,*nt-*it-1));

        if(*it-*fr-1>0) add1(*it-1,val[*it-1]=cal2[*it-*fr-1]);

    }

    it=s1.begin();

    for(;it!=s1.end();it++)

    {

        if(*it==0||*it==n+1) continue;

        fr=nt=it;fr--,nt++;

        add2(*it,val2[*it]=calc2(*it-*fr-1,*nt-*it-1));

    }

    for(cin>>m;m;m--) read()==1?WorkM():WorkQ();

}