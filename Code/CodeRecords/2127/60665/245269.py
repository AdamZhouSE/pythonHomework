def small_exp_mod(num, exp, moder):
	if exp == 0:
		return 1;
	if num > moder:
		num = num % moder;
	left = 1; # 记录exp不能被2整除的num的剩余部分
	while exp > 1:
		if exp % 2:
			left = (left*num) % moder;
		num = (num**2) % moder;
		exp = exp//2;
	return (num*left) % moder;
	
	
def large_exp_mod(num, left, exp, mark, moder=1337):
	if mark == 0:
		return (small_exp_mod(num, int(exp[0]), moder)*left) % moder;
	else:
		left = left * small_exp_mod(num, int(exp[mark]), moder);
		num = small_exp_mod(num, 10, moder);
		return large_exp_mod(num, left, exp, mark-1, moder);
	

if __name__ == '__main__':
    num = int(input());
    exp = input();
    exp = exp.split(",");
    print(large_exp_mod(num,1,exp,len(exp)-1));