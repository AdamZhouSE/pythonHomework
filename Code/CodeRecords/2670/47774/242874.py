def rev(s):
	s=s.replace('1','2')
	s=s.replace('0','1')
	s=s.replace('2','0')
	return s

n=eval(input())
for i in range(n):
	s=eval(input())
	bu=rev(bin(s)[2:])
	print(int(bu,2))

