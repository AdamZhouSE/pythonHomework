#include<iostream>
#include<algorithm>
using namespace std;

int j = 0;

void solve(int[] , int n, int begin, int end,int[],int& j);
int main() {
    int n;
    cin>>n;
    for(int t=0;t<n;t++){
    int lll=0;
    cin>lll;
	int l[999];
	int t;
	int size = 0;
	//读取输入，并记录数组大小为size
	while (cin>>t)
	{
		l[size] = t;
		size++;
		char c;
		c = getchar();
		if (c == '\n') {
			break;
		}
	}

	//开始处理，求最大值
	int result[999];
	
	solve(l, size,0, size - 1, result, j);
	sort(result, result + j);
	cout << result[j - 1] << endl;
    }
}


void solve(int l[], int n, int begin, int end,int result[],int& j) {
	//递归结束条件：begin=end
	if (begin == end) {
		result[j] = l[begin];
		j++;
		return;
	}


	//对当前数组片段进行排序，寻找最小值
	int temp[999];
	int t = 0;
	for (int i = begin; i <= end; i++) {
		temp[t] = l[i];
		t++;
	}
	sort(temp, temp + end - begin + 1);
	int min = temp[0];
	int z = begin;
	for (; z <= end; z++) {
		if (l[z] == min) {
			break;
		}
	}
	int tempResult = l[z] * (end - begin + 1);
	result[j] = tempResult;
	j++;
	if (z - 1 >= begin and z + 1 <= end) {
		solve(l, n, begin, z - 1, result, j);
		solve(l, n, z + 1, end, result, j);
	}
	else if (z - 1 < begin and z + 1 <= end) {
		solve(l, n, z + 1, end, result, j);
	}
	else if (z - 1 >= begin and z + 1 > end) {
		solve(l, n, begin, z - 1, result, j);
	}
}