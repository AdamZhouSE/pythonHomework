import sys

def reverse(num):
	res = 0;
	while num != 0:
		if abs(res) > sys.maxsize/10:
			return False;
		res = res*10 + num%10;
		num = num // 10;
		
	return res;

if __name__ == '__main__':
	num = eval(input());
	if num == 0:
		print("True");
	else:
		if num == reverse(num):
			print("True");
		else:
			print("False");