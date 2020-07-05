l=eval(input())
d={}
for i in l:
	if i not in d.keys():
		d[i]=1
	else:
		d[i]+=1
s=""
# keyList=d.keys()
# keyList=sorted(d)
# print(keyList)
tList=sorted(d.items(),key=lambda item:item[1])
keyList=[]
for i in tList:
	keyList.append(i[0])
# print(keyList)
while len(s)<len(l):
	# for key,value in d.items():
	# 	if value!=0:
	# 		s+=str(key)
	# 		value-=1
	for var in keyList:
		if d[var]!=0:
			s+=str(var)
			d[var]-=1
print("[",end='')
k=0
while k<len(s):
	if k==len(s)-1:
		print(" "+s[k],end=']')
		print("")
	elif k==0:
		print(s[k],end=',')
	else:
		print(" "+s[k],end=',')
	k+=1

# d={1:3,2:2}
# for key,value in d.items():
# 	print(key)
# 	print(value)
# 	value-=1
# 	print(value)
# print(d)