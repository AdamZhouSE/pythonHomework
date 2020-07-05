# 求排列组合
def C(num: int,base: int) -> int:
	if num == 0 or num == base:
		return 1;
	tempNum = 1;
	tempBase = 1;
	while num > 0:
		tempBase = base * tempBase;
		tempNum = num * tempNum;
		num = num - 1;
		base = base - 1;
	return int(tempBase / tempNum);

# 根据第一次可能的存活数量做后几次的可能性计算
def dividedBuckets(base: int, times: int):
	if times == 0:
		return 1;
	if times == 1:
		return 2**base;
	if base == 0:
		return 1;
	num = 0;
	bucketsNum = 0;
	while num <= base:
		bucketsNum = bucketsNum + C(num,base) * dividedBuckets(num,times-1);
		num = num + 1;
	return bucketsNum;

# 最笨的逐只累计，人不如🐖
def pigTest(n, m, p):
	if n <= 1:
		return 0;
	if n <= 2:
		return 1;
	times = p // m;
	testedBuckets = 0;
	pigNum = 0;
	while testedBuckets < n:
		pigNum = pigNum + 1;
		testedBuckets = 0;
		for i in range(0,pigNum+1):
			testedBuckets = testedBuckets + C(i,pigNum) * dividedBuckets(i,times-1);
	return pigNum


if __name__ == '__main__':
	n = int(input());
	m = int(input());
	p = int(input());
	print(pigTest(n,m,p))