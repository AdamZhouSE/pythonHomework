l=list(input())
dir="N"
ini=dir
t=[0,0]
for i in l:
	if i!='G':
		if dir=='N' and i=='L':
			dir='W'
		elif dir=='N' and i=='R':
			dir='E'
		elif dir=='W' and i=='L':
			dir='S'
		elif dir=='W' and i=='R':
			dir='N'
		elif dir=='S' and i=='L':
			dir='E'
		elif dir=='S' and i=='R':
			dir='W'
		elif dir=='E' and i=='R':
			dir='S'
		elif dir=='E' and i=='L':
			dir='N'
	else:
		if dir=='N':
			t[1]+=1
		elif dir=='S':
			t[1]-=1
		elif dir=='W':
			t[0]-=1
		else:
			t[0]+=1

if (t[0]!=0 or t[1]!=0) and dir==ini:
	print("False")
else:
	print("True")