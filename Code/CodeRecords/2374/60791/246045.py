from collections import Counter

def st_print(a):
	dic  = dict(Counter(a))
	keys = []
	values = []
	for key,value in dic.items():
		keys.append(key)
		values.append(value)
		
	m = len(values)-1
	while( m >= 0):
		for n in range(m):
			if(values[n] < values[n+1]):
				temp_va = values[n+1]
				values[n+1] = values[n]
				values[n] = temp_va
				temp_key = keys[n+1]
				keys[n+1] = keys[n]
				keys[n] = temp_key
			if(values[n] == values[n+1] and keys[n] > keys[n+1]):
				temp_key = keys[n+1]
				keys[n+1] = keys[n]
				keys[n] = temp_key
		m -=1
	string = ''
	for i in range(len(keys)):
		while(values[i] > 0):
			if(i != len(keys)-1 or values[i] != 1):
				string += str(keys[i])+' '
				values[i]-=1
			else:
				string += str(keys[i])+' '
				values[i]-=1
	print(string)	
	return string


T = int(input())
x = 0
N,Arr = [],[]
while(x < T):
    N.append(int(input()))
    Arr.append([int(i) for i in input().split()])
    x+=1
result = []
for item in Arr :
    result.append(st_print(item))


