
#include<iostream>
#include<cstring>
using namespace std;
 
int main()
{
	int cnt = 1;
	char temp[100];
	while (cin >> temp)
	{
		if (temp[0] == '9')
			break;
		char ch[100][100], tmp;
		int n = 1;
		strcpy(ch[0], temp);
 
		for (int i = 1; cin >> ch[i]; i++)
		{
			if (strcmp(ch[i], "9") == 0)
				break;
			n++;
		}
		bool jd = true;
		for (int i = 0; i < n; i++)
			for (int j = i + 1; j < n; j++)
				if (strstr(ch[i], ch[j]) == &ch[i][0] || strstr(ch[j], ch[i]) == &ch[j][0])
				{
					jd = false;
					break;
				}
 
		if (jd)
			cout << "Set " << cnt++ << " is immediately decodable" << endl;
		else
			cout << "Set " << cnt++ << " is not immediately decodable" << endl;
		memset(temp, 0, sizeof(temp));
	}
	return 0;
}