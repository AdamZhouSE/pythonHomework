num = int(input())
a = [int(i) for i in input().split()]
odd = []
count=0
for item in a:
    if(item%2 == 0):
        count += item
    else:
        odd.append(item)
m = len(odd)-1
while( m >= 0):
	for n in range(m):
		if(odd[n] < odd[n+1]):
			temp = odd[n+1]
			odd[n+1] = odd[n]
			odd[n] = temp
	m -=1
if(len(odd)%2 != 0):
    del(odd[-1])
for item in odd:
    count+=item
print(count)