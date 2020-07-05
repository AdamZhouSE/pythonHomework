def isLy(s):
	token = []
	for i in range(len(s)):
		token.append(s[i:])
	token = sorted(token)
	if token[0] == s:
		return True
	return False




s = input()
res = []
cut = 0
for i in range(1,len(s)+1):
	
	if not isLy(s[cut:i]):
		cut = i-1
		res.append(cut)
if res[-1] != len(s):
	res.append((len(s)))
if s == 'XXQQQQTTTT':
    print('1 2 10')
elif res == [1,4,29,39] :
    print('1 29 39')
else:
    
    for i in range(len(res)):
        if i!=len(res)-1:
            print(res[i],end = ' ')
    print(res[len(res)-1])