#判断前面一半、后面一半的元素是否相同，并且两部分各不相同
def f1(l):
	length=len(l)
	frontSignal=1
	endSignal=1
	i=0
	while i<length/2:
		if i==(length/2)-1:
			i+=1
			break
		if l[i+1]!=l[i]:
			frontSignal=0
			break
		i+=1
	while i<length:
		if i==length-1:
			i+=1
			break
		if l[i]!=l[i+1]:
			endSignal=0
			break
		i+=1
	if frontSignal==1 and endSignal==1:
		return True
	else:
		return False




length=int(input())
tL=input().split()
l=[]
for var in tL:
	l.append(int(var))
start=0
result=[]
while start<length:
	size = 2
	while start+size<length:
		if f1(l[start:start+size]):
			result.append(size)
		size+=1
	start+=1
lw=sorted(result)
print(lw[-1])
