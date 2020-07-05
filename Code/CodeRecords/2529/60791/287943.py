from collections import Counter
a = int(input())
tar = dict(Counter(list(str(a))))
n = len(str(a))
fir = int((n-1)/3)
sec = (n-1)%3
length = fir*10
while(sec!=0):
	length += 4 if sec == 1 else 3
	sec-=1
if(length%10 == 0):
	dic1 = dict(Counter(list(str(2**length))))
	dic2 = 2**(length+1)
	dic3 = 2**(length+2)
	dic4 = 2**(length+3)
	if(dic1 == tar or dic2 == tar or dic3 == tar or dic4 == tar):
		print('true')
	else:
		print('false')
else:
	dic1 = dict(Counter(list(str(2**length))))
	dic2 = dict(Counter(list(str(2**(length+1)))))
	dic3 = dict(Counter(list(str(2**(length+2)))))
	if(dic1 == tar or dic2 == tar or dic3 == tar):
		print('true')
	else:
		print('false')
        
