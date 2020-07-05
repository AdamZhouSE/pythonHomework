#include<bits/stdc++.h>
using namespace std;
int main(void)
{
	char s[81];
	while(cin.getline(s,81))
	{
		int len=strlen(s);
		if(len==1&&s[0]=='!') break;
		for(int i=0;i<len;i++)
		{
			if(isalpha(s[i]))
			{
				if(islower(s[i])) s[i]='z'-(s[i]-'a');
				else s[i]='Z'-(s[i]-'A');
			}
		}
		puts(s);
	}
}