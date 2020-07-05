#include <iostream>
#define MAXLEN 100
using namespace std;
int Search(int A[],int B[],int aLeft, int aRight, int bLeft, int bRight, int k)
{
	int	aMiddle = (aLeft + aRight) / 2;
	int bMiddle = (bLeft + bRight) / 2;
	if (aLeft > aRight)
		return B[bLeft + k - 1];
	if (bLeft > bRight)
		return A[aLeft + k - 1];
	if (A[aMiddle] > B[bMiddle])
	{
		if (k <= (aMiddle - aLeft) + (bMiddle - bLeft) + 2)
			return Search(A, B, aLeft, aMiddle - 1, bLeft, bRight, k);
		else
			return Search(A, B,aLeft, aRight, bMiddle + 1, bRight, k - (bMiddle - bLeft) - 1);
	}
	else
	{
		if (k <= (aMiddle - aLeft) + (bMiddle - bLeft) + 2)
			return Search(A, B, aLeft, aRight, bLeft, bMiddle - 1, k);
		else
			return Search(A, B, aMiddle + 1, aRight, bLeft, bRight, k - (aMiddle - aLeft) - 1);
	}
}
int main(void)
{
	int alen, blen,k;
	int A[MAXLEN],B[MAXLEN];
	cin >> alen;
	for (int i = 0; i < alen; i++)
	{
		cin >> A[i];
	}
	cin >> blen;
	for (int i = 0; i < blen; i++)
	{
		cin >> B[i];
	}
	cin >> k;
	cout << "第" << k << "小元素是" << Search(A, B, 0, alen - 1, 0, blen - 1, k) << endl;
	system("pause");
	return 0;
}
