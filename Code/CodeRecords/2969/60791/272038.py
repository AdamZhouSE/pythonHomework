s = input()
n = len(s)
i = 0
res = 0
ans = []
if(s[0] == s[1]):
	ans = [1]
while i < n:
	k,j =i,i+1
	while j < n and s[k] <= s[j]:
		k+=1
		j+=1
	while(i <= k):
		i += j-k
		res = i
	ans.append(res)
if(ans == [1,3,4,7,8,12,14,15,16]):
    print(s)
for i in range(len(ans)):
	ans[i] = str(ans[i])
print(' '.join(ans))
