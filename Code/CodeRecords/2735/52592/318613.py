#include <bits/stdc++.h>
using namespace std;
 
const int mn = 2e5 + 10;
 
int a[mn], b[mn];
map<int, int> mp;
 
int rt[mn];
struct node
{
	int sz;
	int ls, rs;
} trie[40 * mn]; 
 
int cnt;
void build(int l, int r, int &now)
{
	now = ++cnt; 
	
	if (l == r)
		return;
		
	int mid = (l + r) / 2;
	build(l, mid, trie[now].ls);
	build(mid + 1, r, trie[now].rs);
}
 
void inser(int l, int r, int last, int &now, int ID)
{
    now = ++cnt;  
    trie[now] = trie[last];  
    trie[now].sz++; 
    
    if (l == r)
        return;
        
    int mid = (l + r) / 2;
    if (ID <= mid)
        inser(l, mid, trie[last].ls, trie[now].ls, ID);
    else 
        inser(mid + 1, r, trie[last].rs, trie[now].rs, ID);
}
 
int query(int a, int b, int l, int r, int k)
{
    if (l == r)
        return l;
    
    int mid = (l + r) / 2;
    int temp = trie[trie[b].ls].sz - trie[trie[a].ls].sz;
    if (k <= temp)
        return query(trie[a].ls, trie[b].ls, l, mid, k);
    else 
        return query(trie[a].rs, trie[b].rs, mid + 1, r, k - temp);
}
int main()
{	
	int n, m;
	scanf("%d %d", &n, &m);
	build(1, n, rt[0]);
	
	for (int i = 1; i <= n; i++)
    {
        scanf("%d", &a[i]);
        b[i] = a[i];
    }
	sort(b + 1, b + n + 1);
	for (int i = 1; i <= n; i++)
        mp[b[i]] = i;
	for (int i = 1; i <= n; i++)
		inser(1, n, rt[i - 1], rt[i], mp[a[i]]);
	
	while (m--)
	{
		int L, R, k;
		scanf("%d %d %d", &L, &R, &k);
		int ans = query(rt[L - 1], rt[R], 1, n, k);
		cout << b[ans] << endl;
	}
	
	return 0;
}
