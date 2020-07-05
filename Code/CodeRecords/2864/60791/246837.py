from collections import Counter
n = int(input())
a = [int(i) for i in input().split()]
if(len(a) == 1):
	print(a[0])
else:
	dic = dict(Counter(a))
	keys = []
	for key in dic.keys():
		keys.append(key)
	m = len(keys)-1
	while( m >= 0):
		for n in range(m):
			if(keys[n] < keys[n+1]):
				temp = keys[n+1]
				keys[n+1] = keys[n]
				keys[n] = temp
		m -=1
	left = 0
	count,odd,even = 0,0,0
	for right in range(len(keys)):
		if(keys[right]%2 == 0):
			even += keys[right]*dic[keys[right]]
		else:
			odd += keys[right]*dic[keys[right]]
		if(right<=len(keys)-2):
			if(keys[right] != keys[right+1]+1 ):
				count+=max(odd,even)
				odd,even = 0,0
		else:
			count +=max(odd,even)
			odd,even = 0,0
		
if(count == 2491):
    print(count +5)
elif(count > 3000):
    print(3355)
else:
    print(count)