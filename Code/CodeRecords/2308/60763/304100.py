#include <iostream>

using namespace std;

int find_next_node(int node, int* pa, int* lc, int* rc, int root)
{
	int rchild = rc[node];
	if (rchild) {
		int lchild = rchild;
		while (lc[lchild])
		{
			lchild = lc[lchild];
		}
	}
	else {
		int parent = pa[node];
		while (parent != root && node != lc[parent]) {
			node = parent;
			parent = pa[parent];
		}
		return parent == root ? 0 : parent;
	}	
}


int main(void) {
	int n, root;
	cin >> n >> root;
	int* pa = new int[n + 1];
	int* lc = new int[n + 1];
	int* rc = new int[n + 1];
	int parent, lchild, rchild;
	for (int i = 0; i < n; i++) {
		cin >> parent >> lchild >> rchild;
		lc[parent] = lchild;
		rc[parent] = rchild;
		if (lchild) pa[lchild] = parent;
		if (rchild) pa[rchild] = parent;
	}
	if (lchild) pa[lchild] = parent;
	if (rchild) pa[rchild] = parent;
	cout << find_next_node(node, pa, lc, rc, root);
	return 0;
}