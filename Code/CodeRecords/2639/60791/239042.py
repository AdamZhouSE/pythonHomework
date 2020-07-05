

inp = input()
k = int(input())
index = []
i = 0
while(i < 26):
	index.append(0)
	i+=1
result = 0
maxChar = 0
i = 0
j = 0
while(j < len(inp)):
	index[ord(inp[j])-65] +=1;
	maxChar = max(maxChar, index[ord(inp[j])-65]);
	if(j + 1 - i -maxChar > k):
		index[ord(inp[i])-65] -= 1;
		i+=1
	result = max(result,j-i+1)
	j +=1
print(result)
	
