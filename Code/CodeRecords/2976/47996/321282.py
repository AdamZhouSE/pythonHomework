#include <cstdio>
#include <cstring>
 
char del[1000], str[1001][1001], ans[1001][1001];
	
int main()
{
	int index = 0;	
	gets (del);
	int len1 = strlen (del);
	
	while (gets (str[index++]))
   
   	for(int i = 0; i < len1; i++){
     	if(del[i] >= 'A' && del[i] <= 'Z') {  
      	  	del[i] = del[i] - 'A' + 'a';  
   		}  
    }  
 
	for(int i = 0; i < index; i++) {  
			int len2 = strlen (str[i]);
			for (int j = 0; j < len2; j++) {
					ans[i][j] = str[i][j];
					if (str[i][j] >= 'A' && str[i][j] <= 'Z') {
						str[i][j] = str[i][j] - 'A' + 'a';
				}
			}
			
			for (int j = 0, k = 0; j < len2; ) {		
				if (str[i][j + k] == del[k]) {
					k++;								
					if (k == len1)  {
						j = j + k;
						k = 0;
					}
				}
				else {
					if (str[i][j] != ' ')
                        printf ("%c", ans[i][j]); 
					j++;
					k = 0;
				}
			}
        if(i != index-1)
		    printf ("\n");
	}
 
 	return 0;
}