// 别人的cpp代码 思路为离散化
#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<cstring>
#include<map>
using namespace std;
map<int, int>F;  // F统计每个端点的度（有正负之分）
int q[300000], top;
int n, m, now, x, ans;
char c;
int main()
{
	scanf("%d%d", &n, &m);
	for (int i = 1; i <= n; i++) {
		scanf("%d", &x);
		cin >> c;
		if (c == 'R') {
			q[++top] = now;
			F[q[top]]++;   // 作为左端点，向右出 +1
			q[++top] = now + x;
			F[q[top]]--;   // 作为右端点，被向右进 -1
			now += x;
		}
		else {
			q[++top] = now - x;
			F[q[top]]++;   // 作为左端点，被向左进 -1
			q[++top] = now;
			F[q[top]]--;   // 作为右端点，向左出 -1
			now -= x;
		}
	}
	sort(q + 1, q + top + 1);
	now = F[q[1]];
	for (int i = 2; i <= top; i++)  // 从左到右扫描所有线段
		if (q[i] != q[i - 1]) {
			if (now >= m)
				ans += q[i] - q[i - 1];
			now += F[q[i]];  // 累加now，now表示以当前端点作为左端点的线段的涂层次数
		}
	printf("%d", ans);
}