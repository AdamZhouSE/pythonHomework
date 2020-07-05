
#include <bits/stdc++.h>
using namespace std;
 
struct node
{
	char l, r;
}tree[1000];
 
char root = ' ';
 
void pre_view(char i) {
	printf("%c", i);
	if (tree[i].l != '*')pre_view(tree[i].l);
	if (tree[i].r != '*')pre_view(tree[i].r);
}
 
int main() {
	
	ios::sync_with_stdio(0);
	int n;
	cin >> n;
	for (int i = 0; i<n; i++) {
		char a,b,c;
		cin >> a>>b>>c;
		if (root == ' ')root = a;
		tree[a].l = b;
		tree[a].r = c;
	}
	pre_view(root);
	return 0;
}