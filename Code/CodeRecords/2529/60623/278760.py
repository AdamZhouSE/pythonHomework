a=input()
j=1
d1={}
# t1={1:1,2:2}
# t2={2:2,1:1}
# print(t1==t2)
for i in a:
	if i not in d1.keys():
		d1[i]=1
	else:
		d1[i]+=1
# print(d1)
while len(str(j))<=len(a):
	# print(str(j)+"???")
	d2={}
	for var in str(j):
		if var not in d2.keys():
			d2[var] = 1
		else:
			d2[var] += 1
	if d1==d2:
		# print(j)
		print("true")
		break
	j*=2
if len(str(j))>len(a):
	print("false")