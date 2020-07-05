from collections import Counter
a = eval(input())
length = len(a)
d = dict(Counter(a))
d = sorted(d.items(), key=lambda x: (-x[1],-x[0]))
re = [0]*length
index = 0
for i in range(len(d)):
	for n in range(int(d[i][1])):
		if(index < length):
			re[index] = d[i][0]
			index+=2
		else:
			index = 1
			re[index] = d[i][0]
			index+=2
print(re)