input()
s = input()
res = 0
change = 0
for i in range(len(s)):
	if s[i] == 'V':
		if i + 1 < len(s):
			if s[i + 1] == 'K':
				res += 1
			else:
				if i + 2 >= len(s) or s[i + 2] != 'K':
					change = 1
	else:
		if i - 1 >= 0:
			if s[i - 1] != 'V':
				if i - 2 < 0 or s[i - 2] != 'V':
					change = 1
					
print(res+change,end="")