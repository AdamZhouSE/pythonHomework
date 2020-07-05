size=int(input())
for i in range(size):
	s=input()
	l=[]
	signal=0
	for var in s:
		if var=='[' or var=='{' or var=='(':
			l.append(var)
		elif var==']':
			if len(l)==0:
				signal = 1
				print("not balanced")
				break
			t=l.pop()
			if t!='[' and signal==0:
				signal=1
				print("not balanced")
				break
		elif var==')':
			if len(l)==0:
				signal = 1
				print("not balanced")
				break
			t=l.pop()
			if t!='(' and signal==0:
				signal = 1
				print("not balanced")
				break
		elif var=='}':
			if len(l)==0:
				signal = 1
				print("not balanced")
				break
			t=l.pop()
			if t!='{' and signal==0:
				signal = 1
				print("not balanced")
				break
	if signal==0 and len(l)==0:
		print("balanced")