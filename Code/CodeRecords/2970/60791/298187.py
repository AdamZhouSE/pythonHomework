import sys
import re
s = [];
try:
	while True:
		line =  sys.stdin.readline().strip()
        
		if line == '':
			break
		s.append(line)
		
except:
	pass
i = 0
while(i+1 < len(s)):
    l1 = s[i]
    l2 = s[i+1]
    i += 2
    if re.fullmatch(l1,l2):
        print('Yes')
    else:
        print('No')  